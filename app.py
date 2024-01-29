from flask import Flask,redirect,url_for,render_template,request,flash,get_flashed_messages
from module.database import Database
from math import ceil

app=Flask(__name__,static_url_path='/static')
app.secret_key= 'secretuserform'

db = Database()

@app.route('/search/')
@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        fname = request.form['fname']
        return redirect(url_for('search',fname=fname))

    per_page = 2  # Number of items per page
    page = int(request.args.get('page', 1))

    data = db.readuser(None)

    total_users = len(data)
    total_pages = ceil(total_users / per_page)

    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    userlist = data[start_index:end_index]

    pagination = {
        'current_page': page,
        'pages': range(1, total_pages + 1)
    }
    return render_template('home_utf8.html',userlist=userlist,messages=get_flashed_messages(),pagination=pagination)

@app.route('/search/<string:fname>/')
def search(fname):
    if fname == '':
        data = db.readuser(None)
    else:
        data = db.readuser(fname)

    return render_template('home_utf8.html',userlist=data,messages=get_flashed_messages())

# Add User routes
@app.route("/add")
def adduserform():
    return render_template('addUser.html')

@app.route("/adduser",methods=['POST'])
def adduser():
    list_hobbies = request.form.getlist('hobbies')
    email = request.form['email']
    if request.method == 'POST':
        if db.create_user(request.form,list_hobbies=list_hobbies,email=email):
            flash('New User Created!')
        else:
            flash('New User Could not be created')

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# Update User Routes
@app.route('/update/<int:id>')
def update(id):
    data = db.readuser(id)
    return render_template('updateUser.html',userinfo=data)

@app.route("/updated-user/<int:id>",methods=['POST'])
def updateuser(id):
    list_hobbies = request.form.getlist('hobbies')
    data = dict(request.form)
    # print(list_hobbies)
    # print(data)
    if request.method == 'POST':
        if db.updateUser(id=id,data=data,list_hobbies=list_hobbies):
            flash('User Updated')
        else:
            flash('User Not updated')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# Delete User Routes
@app.route("/delete/<int:id>")
def delete(id):
    data = db.readuser(id)
    return render_template('deleteConfirmation.html',data=data)

@app.route("/deleteUser/<int:id>",methods=['POST'])
def deleteUser(id):
    if request.method=='POST':
        if db.deleteUser(id):
            flash('User Successfully Deleted')
        else:
            flash('User Could Not Be Deleted')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# port
if __name__ == '__main__':
    app.run(port=5000,debug=True)