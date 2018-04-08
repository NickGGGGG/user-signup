from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_input.html',)

@app.route('/', methods=['POST'])
def testing():

    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    v_password_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter a username'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Please enter a  valid username'

    if password == '':
        password_error = 'Please enter a password'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Please enter a vaild password'
    elif password != v_password:
        password_error = 'Please enter a matching password'
        v_password_error = 'Please enter a matching password'
        
    if v_password == '':
        v_password_error = 'Please enter a password'
    elif len(v_password) < 3 or len(v_password) > 20:
        v_password_error = 'Please enter a valid password'
        
    if email != '':
        if '@' not in email and '.' not in email or len(email) < 4:
            email_error = 'Please enter a valid email'
        
    if username_error == '' and password_error == '' and v_password_error == '' and email_error == '':
        return redirect('/welcome?username={0}'.format(username))


    return render_template('user_input.html',username=username,
        username_error=username_error,
        password_error=password_error,
        v_password_error=v_password_error,
        email_error=email_error,
        email=email)

@app.route('/welcome')
def welcome():
    
    username = request.args.get('username')
    return render_template('welcome.html',username=username)


app.run()