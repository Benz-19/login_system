from flask import Flask, render_template, request, redirect
from login_system import User

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User()
    username = request.form['username'].strip().lower()
    password = request.form['password']
    hashed_pass = password
    print(username, hashed_pass)
    if user.login_user(username.capitalize(), hashed_pass):
        return f"<h1>Welcome, {username}</h1>"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run(debug=True)
