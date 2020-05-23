import webbrowser
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
    with open("Usernames.txt" , "r+") as f:
        with open("Password.txt", "r+") as P:
            if username in f.readlines() and password in P.readlines():
                webbrowser.open("google.com")
                return
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
    new_username = input("New Username: ")
    new_password = input("New Password: ")
    with open("Usernames.txt", "r+") as f:
        for line in f.readlines():
            if line.strip() == new_username:
                print("Error. Try again")
                return register()
        else:
            f.write("\n" + new_username)
            with open("Password.txt", "r+") as p:
                p.write("\n" + new_password)
            p.close()
    f.close()
    login()
main_page()
