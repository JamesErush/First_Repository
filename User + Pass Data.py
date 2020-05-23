import webbrowser
user_names_data = open("Usernames.txt", "r+")
passwords_data = open("Password.txt", "r+")
Usernames = ["James"]
Passwords = ["Rush"]
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
    #user_names_data = open("Usernames.txt", "r+")
    #passwords_data = open("Password.txt", "r+")
    if username in Usernames and password in Passwords:
        webbrowser.open("https://www.google.com")
    else:
        print("Not a Valid Username or Password.")
        decision = input("Would you like to try again or create a new account?")
        decision = decision.lower()
        if decision == "try again":
            login()
        elif decision == "new account":
            register()
        else:
            print("Invalid Response please write either try again or new account.")
            login()

def register():
    Created_Username = (input("New Username: "))
    Created_Password = (input("New Password: "))
    if Created_Username in Usernames:
        new_username = input("Username already taken. Please enter a different Username: ")
        Usernames.append(new_username)
        Created_Password = (input("New Password: "))
        Passwords.append(Created_Password)

    else:
        Usernames.append(Created_Username)
        Passwords.append(Created_Password)
    #username = (input("New Username: "))
    # if username in user_names_data:
        # username = input("Username already taken. Enter a new Username: ")
        #user_names_data.write(username + "\n")
        #user_names_data.close()
        #password = (input("New Password: "))
        #passwords_data.write(password + "\n")
        #passwords_data.close()
    #else:
        #user_names_data.write(username + "\n")
        #password = input("New Password: ")
        #passwords_data.write(password + "\n")
        #passwords_data.close()
    login()

main_page()




