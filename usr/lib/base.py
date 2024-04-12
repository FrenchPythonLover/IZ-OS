from rich.console import Console
from rich.prompt import Prompt
console = Console(color_system="truecolor")
from rich import print
version = "IZOS VERSION 5"
def klog(text):
    print(f"[ KERNEL ] {text}")
user = "root"
netname = "izos"
commands = ["ls","cls","clear","help"]
creds = "IZOS V5 1 by ilyes"