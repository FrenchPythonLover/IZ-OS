import sys
sys.path.append("../lib/")
import base
import os
try:
    print(f"[red bold]Deleting {shell[1]}.py...")
    try:
        if shell[1] == "delbin" or shell[1] == "pm":
            print("[red]You cannot delete system files ! :)")
            break
        os.remove(f"usr/bin/{shell[1]}.py")
        
    except Exception as e:
        print("[red bold]No such file !")
        print(e)
        print(os.listdir())
except:
    print("""
delbin: Delete your programs in one command!
usage: delbin <package name>
example: delbin test
[red bold]Please specify an argument !
    """)