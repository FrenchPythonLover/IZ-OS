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
                print(os.listdir(shell[1]))
        except:
            if directory == "/":
                print(os.listdir("./"))
            else:
                print(os.listdir(directory))
    # if shellnoarg == "cd":
    #     try:
    #         if os._exists(shell[1]):
    #             directory = shell[1]
    #         else:
    #             print("[red]ERROR: No such directory")
    #             r
    #     except Exception as e:
    #         print("[red]ERROR: please specify directory")
    #         print(e)
    if commands.__contains__(shellnoarg) == False:
        try:
            with open(f"./usr/bin/{shellnoarg}.py", "r") as bin:
                exec(bin.read())
        except:
            print("[red]Error: No such executable file found.")
    