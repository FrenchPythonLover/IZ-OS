######### IZOS NEW KERNEL
# Start >> include default libs

isroot=False # A bool saying if user is root or not
import sys,warnings
sys.path.append("./lib/")
from izos import *
import tmp
# Start >> Testing terminal colors. (yellow,red,green,blue)
warn("color test")
error("color test")
ok("color test")
info("color test")
time.sleep(2)
# Start >> Launching the init file 
with open(initsystem,"r") as initrc:
    exec(initrc.read())
info("Putting up shell variables")
prefix = "$" # Either $ (user) or # (root)
izosdir = ""
dir = './'+izosdir #current dir
currentusr = f"{data.name}" # Current user
ok("Shell variables done.")
with open(loginsystem) as login:
    exec(login.read())
if not logon:
    error("You are not logged in. Either Wrong Password Or Username")
    exit()
ok("Welcome To IZOS !")
# Shell Code

while True:
    try:  
        cmdlist = [f for f in os.listdir("./shell") if os.path.isfile("./shell"+'/'+f)] # Refreshing every shell commands (put there for dev)
        shstring = f"{currentusr}@{data.hostname} {dir} {prefix} :" # Complete shell string 
        commandargs = input(shstring).split(" ")
        command = commandargs[0] # Just the first string, other considered as args
        if command != "":
            for i in range(len(cmdlist)):
                if cmdlist[i].replace(".py","") == command:
                    tmp.a = 1
            if tmp.a == 0 or tmp.a == None: ## Deduct if there is usr/bin apps or sum????
                appsfiles = next(os.walk("./usr/bin/"), (None, None ,[]))[2] # WTF
                for i in range(len(appsfiles)):
                    if command == appsfiles[i].replace(".py",""):
                        tmp.b = 1
            if tmp.a == 1:
                tmp.a = 0
                with open(f"./shell/{command}.py","r") as shcmd:
                    exec(shcmd.read())
            elif tmp.b == 1:
                tmp.b = 0
                with open(f"./usr/bin/{command}.py","r") as appcmd:
                    exec(appcmd.read())
            else:
                print("[red bold]File is in apps or not exists[/red bold]")
        else:
            pass
    except Exception as ex:
        ######## KERNEL PANIC !
        os.system("cls" if os.name == "nt" else "clear") # clear
        print("0x464154414c")
        print("70 65 84 65 76")
        print("1000110 1000001 1010100 1000001 1001100")
        print("Kernel Panic: Attempted to kill kernel.py !")
        print(f"Code: {ex}")
        exit()