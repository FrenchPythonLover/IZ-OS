import sys
import os
import time
sys.path.append("./usr/lib/")
from base import *
klog("Imported base library !")
klog("Booting...")
klog("[green bold]Welcome to IZOS !")
time.sleep(1)
directory = "/"
while True:#After boot code: The "real" system
    if user == "root":
        shells = f"root@{netname} {directory} # "
    else:
        shells = f"{user}@{netname} {directory} $ "
    shell = Prompt.ask(shells).split(maxsplit=-1)
    if shell == []:
        pass # just dont do anything because there isn't input
    else:
        shellnoarg = shell[0]
        if shellnoarg == "exit" or shellnoarg == "stop":
            exit()
        if shellnoarg == "clear" or shellnoarg == "cls":
            os.system('cls' if os.name=='nt' else 'clear')
        if shellnoarg == "help":
            print(commands)
        if shellnoarg == "ls":
            try: 
                if shell[1] == "/":
                    print(os.listdir("./"))
                else:                  
                    # I swear this is the worst hack ever... But it works!
                    # (mentalité programmeur)
                    try:
                        print(os.listdir(shell[1]))
                    except:
                        print("[red]ERROR: No such directory ! Please execute the following command:\n[/red][blue]cd ./") 
            except:
                if directory == "/":
                    print(os.listdir("./"))
                else:
                    try:
                        print(os.listdir(directory))
                    except:
                        print("[red]ERROR: No such directory ! Please execute the following command:\n[/red][blue]cd ./")
        if shellnoarg == "cd":
            try: # i literally took the code from version 4.9 to got this working and i didn't notice it until i pushed it...
                #al hamdoulilah :)
                ls = os.listdir()
                directory = shell[1]
            except:
                print("No such directory !")
        if commands.__contains__(shellnoarg) == False:
            try:
                with open(f"./usr/bin/{shellnoarg}.py", "r") as bin:
                    exec(bin.read())
            except:
                print("[red]Error: No such executable file found.")
        