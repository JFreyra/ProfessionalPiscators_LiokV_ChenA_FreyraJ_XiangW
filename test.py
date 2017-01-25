<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)
=======
from flask import Flask, render_template, url_for, request, redirect, session, flash
from utils import flaskUtils

def redirect_url():
    return request.referrer or url_for("index")

app = Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyz"
>>>>>>> c5a6a688ad594cd8ed5cce781053a867c62581cc

@app.route('/')
def index():
    return render_template("test.html")

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(debug=True)
=======

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else: #assert method is POST
        username = request.form.get("username")
        password = request.form.get("password")
        '''
        DB function needed: isValidLogin(username, password)
        * return False if login unsuccessful, if:
            * username doesn't exist
            * username does exist, but password wrong
        * return True otherwise
        '''
        if isValidLogin(username, password):
            '''
            DB function needed: getUserID(username)
            * given username, get user ID
            '''
            #user_id = getUserID(username)
            #session["user_id"] = user_id
            flash('Login successful!', 'success')
            return redirect('/')
        
        else:
            flash("Login unsuccessful! Please create an account if you haven't already!", 'error')
            return render_template("login.html")

    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else: #assert method is POST
        username = request.form.get("username")
        password = request.form.get("password")
        name_first = request.form.get("firstname")
        name_last = request.form.get("lastname")
        '''
        DB function needed: isValidRegister(username, password, password_confirm)
        * return False if registration unsuccessful, if:
            * username already exists
        * return True otherwise
        '''
        if isValidRegister(username, password):
            '''
            DB function needed: addUser(username, password, firstname, lastname)
            * return nothing lmao
            '''
            #addUser(username, password, firstname, lastname)
            
            #user_id = getUserID(username)
            #session["user_id"] = user_id
            flash('Registration successful!', 'success')
            return redirect('/')
        
        else:
            flash('Registration unsuccessful! Username probably already exists!', 'error')
            return render_template("register.html")


@app.route('/todo')
#Frontend sends AJAX request (POST) to /todo every time todo list changed
def todo( methods=['POST'] ):
    return request.args.get('')
       
    return ""


@app.route('/logout')
def logout():
    if "user_id" in session:
        session.pop("user_id")
    else:
        flash('Not logged in yet!', 'error')
    return redirect(flaskUtils.redirect_url())


if __name__ == "__main__":
    app.run( debug=True, port=6969 );
>>>>>>> c5a6a688ad594cd8ed5cce781053a867c62581cc