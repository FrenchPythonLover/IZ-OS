from rich.console import Console
from rich.prompt import Prompt
import os
console = Console(color_system="truecolor")
from rich import print
version = "IZOS VERSION 5"
def klog(text):
    print(f"[ KERNEL ] {text}")
user = "root"
netname = "izos"
# commands = ["ls","cls","clear","help"]
creds = "IZOS V5 1 by ilyes"

def ls(args, directory):
    dir_path = args[1] if args[1] != "/" else "./"

    try:
        dir_list = os.listdir(dir_path)
        print("\n".join(dir_list))
    except:
        dir_list = os.listdir(dir_path if args[1] != "/" else directory)
        print("\n".join(dir_list))

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