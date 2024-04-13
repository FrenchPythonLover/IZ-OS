import sys, os, time

sys.path.append("./usr/lib/")
from base import *

# Logs
klog("Imported base library !")
klog("Booting...")
klog("[green bold]Welcome to IZOS !")
time.sleep(1)
directory = "/"
while True:#After boot code: The "real" system
    suffix = "#" if user == "root" else "$"

    shells = f"root@{netname} {directory} {suffix} "
    args = Prompt.ask(shells).split(maxsplit=-1)
    cmd_name = args[0]

    for command in COMMANDS:
        for name in command["names"]:
            if name == cmd_name:
                command["exec"](args, directory)


    # match cmd_name:
    #     case "exit":
    #         exit()
        
    #     case "stop":
    #         exit()

    #     case "clear":
    #         os.system('cls' if os.name=='nt' else 'clear')

    #     case "cls":
    #         os.system('cls' if os.name=='nt' else 'clear')

    #     case "help":
    #         print(commands)

    #     case "ls":
    #         try:
    #             if shell[1] == "/":
    #                 print(os.listdir("./"))
    #             else:
    #                 print(os.listdir(shell[1]))
    #         except:
    #             if directory == "/":
    #                 print(os.listdir("./"))
    #             else:
    #                 print(os.listdir(directory))



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
    if commands.__contains__(cmd_name) == False:
        try:
            with open(f"./usr/bin/{cmd_name}.py", "r") as bin:
                exec(bin.read())
        except:
            print("[red]Error: No such executable file found.")
    