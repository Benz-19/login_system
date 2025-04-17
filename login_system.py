import sqlite3
import connection
import hashlib

class User:
    def validate_input(self, message):
        while True:
            value = input(message)
            try:
                value = int(value)
                break
            except ValueError:
                    print("Ensure the input value a whole number")
        return value

    def hash_password(self, password):
        return hashlib.sha256(str(password).encode()).hexdigest()

    def get_user_db_data(self, name, password):
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


    def login_user(self, name, password):
        try:
            user = self.get_user_db_data(name, password)
            if user["username"] == name and user["password"] == str(password):
                return True
            else:
                return False
        except UserWarning as e:
            print(f"Failed to login user... ErrorType: {e}")


    def create_user(self, name, password):
        try:
            hashed_password = self.hash_password(password)
            connection.cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", (name, str(hashed_password)))
            connection.conn.commit()
            print("User was created successfully...")
        except sqlite3.IntegrityError:
            print("Username already exists. Please try a different one.")
        except UserWarning as e:
            print(f"Failed to create user... ErrorType: {e}")


    def user_dashboard(self, name):
        print(f"\n--------Welcome {name} ----------")

    def get_user_sign_in(self):
        user_name = input("Username = ")
        user_password = user.validate_input("Password: ")
        if self.login_user(user_name.capitalize(), user_password):
            self.user_dashboard(user_name.strip())
        else:
            print("Login failed... Quiting...")
            exit()


# Sign-in
user = User()
def ui_component():
    validate = True
    print("Use 1 and 2 to select an option.\n[1] Login\n[2] Create an account")
    while validate:
        response = user.validate_input("Response >> ")
        match response:
            case 1:
                user.get_user_sign_in() #logins the user
                validate = False
            case 2:
                name = input("Enter your name >> ")
                password = user.validate_input("Password >> ")
                user.create_user(name, password) #creates a new user
                validate = False
            case _:
                print("Only valid options 1,2 can be selected...")


ui_component()
