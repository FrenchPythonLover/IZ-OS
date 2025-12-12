### LOGINPY V1
print("LOGIN SHELL")
import data
username = input("User:").lower()
password = input(f"Password for user {username}: ").lower()
if username:
    if password:
        if username == data.name:
            if hashlib.sha256(password.encode("utf-8")).hexdigest() == data.passwd:
                
                print("Logon Successful")
                logon = True
            else:
                print("Wrong pass")
                exit()
        else:
            print("Wrong user")
            exit()
    else:
        print("No password ?!")
        exit()
else:
    exit()