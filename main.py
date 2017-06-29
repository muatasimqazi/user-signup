from flask import Flask, request, redirect, render_template
import cgi, re

app = Flask(__name__)
app.config['DEBUG'] = True



def valid_username(username):
    return re.search("^[A-z][A-z|\.|\s]+$", username) != None

def valid_password(password):
    return re.search(r"[a-z]", password) or re.search(r"[!@$&]", password) or re.search(r"[A-Z]", password) or re.search(r"\d", password)

def valid_email(email):
    return re.search(r'[\w.-]+@[\w.-]+.\w+', email)

@app.route('/', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verfiy-password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verfiy_error = ''
    email_error = ''

    if not valid_username(username):
        username_error = "That's not a valid username"
    if not valid_password(password) and verify == '':
        password_error = "That's not a valid password"
    if verify != password:
        verfiy_error = "Passwords don't match"
        password_error = ''
    if not valid_email(email) and len(email) > 0:
        email_error = "That's not a valid email"
    if not (username_error or password_error or verfiy_error or email_error):
        return redirect('/welcome?username=' + username)
    else:
        return render_template('index.html',
            username_error = username_error,
            password_error = password_error,
            verfiy_error = verfiy_error,
            email_error = email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    return render_template('index.html',
    username_error = '',
    password_error = '',
    verfiy_error = '',
    email_error = '')
app.run()
