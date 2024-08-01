# username
# password

username = input("Username >>>")
password = input("Password >>>")

regular_user_password = "qwerty"

if "admin" in username:
    print("Welcome to website, admin")
else:
    if len(username) > 5:
        print("Welcome")
    else:
        print("Bad username")