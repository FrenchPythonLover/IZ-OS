import sys
import urllib.request
import os
sys.path.append("../lib")
import base
from base import print
try:
    arg = shell[1]
    if shell[1] == "install":
        try:
            if shell[2] == "-s":
                print(f"Saving {shell[4]}.py using custom repo {shell[3]}..")
                urllib.request.urlretrieve(f"{shell[2]}{shell[3]}.py", f"usr/bin/{shell[3]}.py")
            else:
                print(f"Saving {shell[2]}...")
                urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/{shell[2]}.py", f"usr/bin/{shell[2]}.py")
        except:
            print(f"[red bold]ERROR: No such file !")
    elif shell[1] == "installbase":
        print("installing base packages..")
        packages = ["calc","cat","python"]
        for i in range(packages.__len__()):
            print(f"[blue bold]Installing {packages[i]}")
            urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSBASEAPPS/main/{packages[i]}.py", f"usr/bin/{packages[i]}.py")
    elif arg == "removebase":
        try:
            print("Removing base...")          
            os.remove("usr/bin/calc.py")
            os.remove("usr/bin/python.py")
            os.remove("usr/bin/cat.py")
        except Exception as e:
            print(f"[red]ERROR: You don't have any installed software !")
except Exception as e:
    print(f"""
pm: a package manager for IZOS !
usage: pm install <package name> / pm installbase
pm install <shell> <package name>
shell: -s:specify an raw githubusercontent url [bold]without the filename[/bold].if not specified, use the https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/ repo.
example:
pm test
or
pm install -s https://raw.githubusercontent.com/ExampleUser/ExampleRepo/ExampleBranch/ test
---
pm installbase: Install base packages. For example the package [blue]calc.
pm removebase: undo the installbase operation
[red bold]Please specify a package name !
    """)