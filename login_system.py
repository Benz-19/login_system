
def validate_input(msg):
    while True:
        request = input(f"{msg}")
        try:
            request = int(request)
            break
        except ValueError:
            print("Ensure your input value is a valid whole number")
            
def login_user(name, password):
    pass

def create_user(name, password):
    pass

def user_dashboard():
    pass

def get_user_sign_in():
    user_name = input("Username = ")
    user_password = validate_input("Password: ")

    if login_user(str(user_name), str(user_password)):
        user_dashboard()