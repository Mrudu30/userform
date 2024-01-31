from flask import Flask,redirect,url_for,render_template,request,flash,get_flashed_messages,jsonify
from module.database import Database
from math import ceil

app=Flask(__name__,static_url_path='/static')
app.secret_key= 'secretuserform'

db = Database()

# home route
@app.route('/search/',methods=['POST','GET'])
@app.route('/',methods=['POST','GET'])
def home():
    print(request.form)
    data = db.readuser(id=None,fname=None)

    form_type = request.form.get('form_type')

    if request.method == 'POST':
        if form_type == 'search':
            print(request.form)
            fname = request.form['fname']
            return redirect(url_for('search',fname=fname))
        elif form_type == 'sort':
            ord = []
            order = request.form['order']
            filter = request.form['filter-order']
            ord.append(order)
            ord.append(filter)
            # print("app\n",order)
            data = db.sort(order=ord)
            print(data)

    # pagination
    per_page = 5  # Number of items per page
    page = int(request.args.get('page', 1))

    print(data)

    total_users = len(data)
    total_pages = ceil(total_users / per_page)

    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    userlist = data[start_index:end_index]
    print("\nuserlist\n",userlist)
    pagination = {
        'current_page': page,
        'pages': range(1, total_pages + 1)
    }
    return render_template('home_utf8.html',userlist=userlist,messages=get_flashed_messages(),pagination=pagination)

# search route
@app.route('/search/<string:fname>/')
def search(fname):
    if fname == '':
        data = db.readuser(fname=None,id=None)
    else:
        data = db.readuser(fname=fname,id=None)

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
    data = db.readuser(id=id,fname=None)
    return render_template('updateUser.html',userinfo=data)

@app.route("/updated-user/<int:id>",methods=['POST'])
def updateuser(id):
    list_hobbies = request.form.getlist('hobbies')
    email = request.form['email']
    data = dict(request.form)
    # print(list_hobbies)
    # print(data)
    if request.method == 'POST':
        if db.updateUser(id=id,data=data,list_hobbies=list_hobbies,email=email):
            flash('User Updated')
        else:
            flash('User Not updated')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# Delete User Routes
@app.route("/delete/<int:id>")
def delete(id):
    data = db.readuser(id=id,fname=None)
    print(data)
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