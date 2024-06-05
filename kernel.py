import sys, os, time
sys.path.append("./usr/lib/")
from base import *

# Logs
klog(f"Booting [green]IZOS {version}-{subver}")
klog("Imported base library !")
klog("Booting...")
klog("[green bold]Welcome to IZOS !")
time.sleep(1)
while True:#After boot code: The "real" system
    with open("usr/lib/data","r+") as d:
        directory = d.read().replace("./","/",1)
    suffix = "#" if user == "root" else "$"
    shells = f"root@{netname} {directory} {suffix} "
    args = Prompt.ask(shells).split(maxsplit=-1)
    cmd_name = args[0]
    for command in COMMANDS:
        for name in command["names"]:
            if name == cmd_name:
                command["exec"](args)
    
    if commands2.__contains__(cmd_name) == False:
        try:
            with open(f"./usr/bin/{cmd_name}.py", "r") as bin:
                exec(bin.read())
        except Exception as e:
            print("[red]Error: No such executable file found.")
    