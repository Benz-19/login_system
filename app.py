from flask import Flask, render_template, request, redirect, url_for,session
from login_system import User

app = Flask(__name__)

app.secret_key = '123456789'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User()
    username = request.form['username'].strip().capitalize()
    password = request.form['password']
    hashed_pass = user.hash_password(password)

    print(username, hashed_pass)
    if user.login_user(username.capitalize(), hashed_pass):
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Login failed"

@app.route('/dashboard')
def dashboard():
        username = session['username']
        if username:
            return render_template('dashboard.html', username = username)
        else:
            return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
