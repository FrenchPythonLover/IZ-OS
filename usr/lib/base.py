from rich.console import Console
from rich.prompt import Prompt
import os
console = Console(color_system="truecolor")
from rich import print
version = 5.3
def klog(text):
    print(f"[ KERNEL ] {text}")
user = "root"
netname = "izos"
commands2 = ["ls","cls","clear","help"]
creds = "IZOS V5 1 by ilyes"

def ls(args, directory):
            try:
                dr = os.listdir(args[1].replace("./","/").replace("/","./"))
                print(dr[::1])
            except:
                print(os.listdir(directory.replace("/","./")))

COMMANDS = [
    {
        "names": ["clear", "cls"],
        "exec": lambda args, _:
            os.system('cls' if os.name=='nt' else 'clear')
    },
    {
        "names": ["exit", "stop"],
        "exec": lambda args, _:
            exit()
    },
    {
        "names": ["ls"],
        "exec": ls
    },
]
