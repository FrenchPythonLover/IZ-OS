# IZOS Setup
dev = False # Dev only mode to skip importants steps (installing modules for ex.) faster -- DO NOT ENABLE
import os, sys, hashlib, shutil,json

print("---- IZOS Setup ----")
print("Installing modules...")
if not dev: os.system("pip install rich psutil --break-system-packages");import rich ## FIXME: Maybe a little risk installing with --break-system-packages...  
print("Checking for already installed system")
sys.path.append("./lib/")
def clean():
        shutil.rmtree("./usr/")
        os.mkdir("./usr/")
        os.mkdir("./usr/bin/")
        os.mkdir("./usr/lib")
if os.path.exists('./lib/data.py'):
    import data
    print("You can't install on top of existing install. do you want to delete current installation? (y/n)")
    if input("(y/n): ").lower() == "y":
        os.remove("./lib/data.py")
        # remove apps directory
        clean()
        print("Now restart the setup")
    else:
        print("Goodbye !")
else:
    print("Not installed; Installing...")
    hostname = input("Hostname Here:")
    user = input("User Name Here:").lower()
    passwd = input("Input password:")
    rootpwd = hashlib.sha256(input("Please put a root password:").encode('utf-8'))
    if user and user != 'root' and passwd and rootpwd:
        print("Hashing Password...")
        hashedpwd = hashlib.sha256(user.encode('utf-8'))
        print("Pushing to data file...")
        with open("./lib/data.py","a+") as datafile:
            datacontent = f"""
# IZOS userdata
# variables
name = "{user}" # UserName
passwd = "{hashedpwd.hexdigest()}" # user password, in sha256
rootpasswd = "{rootpwd.hexdigest()}" # root password, in sha256
hostname = "{hostname}"
            """
            datafile.write(datacontent) 
    elif user=='root':
        print("[bold]root[/bold] username is already taken !")
    elif not passwd or not rootpwd:
        print("Please put a password")
    elif not user:
        print("Please put a username")
