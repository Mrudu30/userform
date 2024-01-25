from flask import Flask,redirect,url_for,render_template,request,flash,get_flashed_messages
from module.database import Database

app=Flask(__name__,static_url_path='/static')
app.secret_key= 'secretuserform'

db = Database()

@app.route('/')
def home():
    data = db.readuser(None)
    return render_template('home_utf8.html',userlist=data,messages=get_flashed_messages())

# Add User routes
@app.route("/add")
def addfr():
    return render_template('addUser.html')

@app.route("/adduser",methods=['POST'])
def adduser():
    list_hobbies = request.form.getlist('hobbies')
    if request.method == 'POST':
        if db.create_user(request.form,list_hobbies=list_hobbies):
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