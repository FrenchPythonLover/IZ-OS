#### SU PROGRAM
import hashlib, data
from rich.prompt import Prompt
import tmp# Import the su var cache from lib/tmp
if tmp.s==0:
    rootpasswd = input("Enter your root password:")
    if hashlib.sha256(rootpasswd.encode('utf-8')).hexdigest() == data.rootpasswd:
        isroot = True
        prefix = "[red]#[/red]"
        print("Successfuly changed the user to root")
        tmp.s=1
        currentusr = "root"
    else:
        print("Su: authentication failure")
else:
    tmp.s=0
    prefix="$"
    isroot=False
    currentusr = data.name