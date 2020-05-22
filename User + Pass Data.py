import webbrowser
user_names_data = open("Usernames.txt", "r+")
passwords_data = open("Password.txt", "r+")

def main_page():
    user_intention = (input("Would you like to Login or Register?"))
    user_intention = user_intention.upper()
    if user_intention == "LOGIN":
        login()
    elif user_intention == "REGISTER":
        register()
    else:
        print("Not a Valid Command. Please choose one of the Listed Options")
        main_page()

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in user_names_data and password in passwords_data:
        webbrowser.open("https://www.google.com")
    else:
        print("Not a Valid Username or Password.")
        decision = input("Would you like to try again or create a new account?")
        decision = decision.lower()
        if decision == "try again":
            login()
        elif decision == "new account":
            register()

def register():
    new_username = input("New Username: ")
    if new_username in user_names_data:
        print("Username already taken. Enter a new Username:")
        new_password = input("New Password: ")
        passwords_data.write(new_password + "\n")
        passwords_data.close()
    else:
        user_names_data.write(new_username + "\n")
        user_names_data.close()
        new_password = input("New Password: ")
        passwords_data.write(new_password + "\n")
        passwords_data.close()

    login()

main_page()




