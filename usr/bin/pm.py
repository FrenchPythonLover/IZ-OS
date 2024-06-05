import sys
import urllib.request
sys.path.append("../lib")
import base
from base import print
try:
    arg = args[1]
    if args[1] == "install":
        try:
            if args[2] == "-s":
                print(f"Saving {args[4]}.py using custom repo {args[3]}..")
                urllib.request.urlretrieve(f"{args[2]}{args[3]}.py", f"usr/bin/{args[3]}.py")
            else:
                print(f"Saving {args[2]}...")
                urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/{args[2]}.py", f"usr/bin/{args[2]}.py")
        except:
            print(f"[red bold]ERROR: No such file !")
    elif args[1] == "installbase":
        print("installing base packages..")
        packages = ["calc","cat","python"]
        for i in range(packages.__len__()):
            print(f"[blue bold]Installing {packages[i]}")
            urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSBASEAPPS/main/{packages[i]}.py", f"usr/bin/{packages[i]}.py")
                    
except:
    print("""
pm: a package manager for IZOS !
usage: pm install <package name> / pm installbase
pm install <args> <package name>
args: -s:specify an raw githubusercontent url [bold]without the filename[/bold].if not specified, use the https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/ repo.
example:
pm test
or
pm install -s https://raw.githubusercontent.com/ExampleUser/ExampleRepo/ExampleBranch/ test
---
pm installbase: Install base packages. For example the package [blue]calc.
[red bold]Please specify a package name !
    """)