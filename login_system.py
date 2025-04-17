import sqlite3
import connection
import hashlib

def validate_input(message):
    while True:
        value = input(message)
        try:
            value = int(value)
            break
        except ValueError:
                print("Ensure the input value a whole number")
    return value

def hash_password(password):
    return hashlib.sha256(str(password).encode()).hexdigest()

def get_user_db_data(name, password):
    try:
        connection.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (name, password))
        user = connection.cursor.fetchone()
        if user:
            return user
        else:
            print ("no user with this data")
            exit()
    except UserWarning as e:
        print(f"Something went wrong, no user data found... ErrorType: {e}")


def login_user(name, password):
    try:
        user = get_user_db_data(name, password)
        if user["username"] == name and user["password"] == password:
            return True
        else:
            return False
    except UserWarning as e:
        print(f"Failed to login user... ErrorType: {e}")


def create_user(name, password):
    try:
        hashed_password = hash_password(password)
        connection.cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", (name, str(hashed_password)))
        connection.conn.commit()
        print("User was created successfully...")
    except sqlite3.IntegrityError:
        print("Username already exists. Please try a different one.")
    except UserWarning as e:
        print(f"Failed to create user... ErrorType: {e}")


def user_dashboard(name):
    print(f"\n--------Welcome {name} ----------")

def get_user_sign_in():
    user_name = input("Username = ")
    user_password = input("Password: ")
    if login_user(user_name.capitalize(), str(user_password)):
        user_dashboard(user_name)
    else:
        print("Login failed... Quiting...")
        exit()


# Sign-in
create_user("Tobi", 55555)
# get_user_sign_in()
