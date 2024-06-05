from rich.console import Console
from rich.prompt import Prompt
import re
from pathlib import Path
import os
console = Console(color_system="truecolor")
from rich import print
version = 5.4
subver = "stable"
data = "./usr/lib/data"
#### Boot code
os.remove(data)
with open(data,"a+") as dfile:
    dfile.write("./root/")
#### End of boot code
def klog(text):
    print(f"[ KERNEL ] {text}")
user = "root"
netname = "izos"
commands2 = ["ls","cls","clear","help","cd","echo","mkdir","touch","rm"]
def cd(args):
    try:
        with open(data,"a+") as file:
            d = file.read()
        
        if args[1][0] == "/" or args[1] == "../":
            if args[1] == "../":
                print("[red]Please type the full path !")
            else:
                print("[red]Your request was blocked!\nInstead of using /, try using ./ !")
        else:
            os.remove(data)
            with open(data,"a+") as file:
                try:
                    os.listdir(args[1])
                    file.write(args[1])
                except:
                    print("[red]Directory doesn't exists!")
                
    except Exception as e:
        print(e)

def ls(args):
    try:
        with open(data,"r") as file:
            d = file.read()
        lsd = os.listdir(d)
        print("\n".join(lsd))
    except Exception as e:
        print(f"[red]ERROR: No such directory !")
def mkdir(args):
    try:
        print("[blue]Info:Always use a complete path while creating dirs !")
        os.mkdir(args[1])
    except:
        print("[red]ERROR:Please specify an argument !")
def touch(args):
    try:
        print("[blue]Info:Please Always use a complete path while creating a file !")
        Path(args[1]).touch()
    except:
        print("[red]Eror: Please specify an argument !")
def rm(args):
    try:
        os.remove(args[1])
    except Exception:
        print("[red]Please specify an argument")
COMMANDS = [
    {
        "names": ["clear", "cls"],
        "exec": lambda args:
            os.system('cls' if os.name=='nt' else 'clear')
    },
    {
        "names": ["exit", "stop"],
        "exec": lambda args:
            exit()
    },
    {
        "names": ["ls"],
        "exec": ls
    },
    {
        "names": ["cd"],
        "exec": cd
    },
    {
        "names": ["echo"],
        "exec": lambda args:
            print(' '.join(args[1::1]))
    },
    {
        "names": ["mkdir"],
        "exec": mkdir
    },
    {
        "names": ["touch"],
        "exec": touch
    },
    {
        "names": ["rm"],
        "exec": rm
    },
    {
        "names": ["help"],
        "exec": lambda args:
        print("\n".join(commands2))
    }
]
