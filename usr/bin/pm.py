import sys
import urllib.request
sys.path.append("../lib")
import base
from base import print
try:
    arg = args[1]
    try:
        if args[1] == "-s" or args[1][1] == "-":
            print(f"Saving {args[3]}.py using custom repo {args[2]}..")
            urllib.request.urlretrieve(f"{args[2]}{args[3]}.py", f"usr/bin/{args[3]}.py")
        else:
            print(f"Saving {args[1]}...")
            urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/{args[1]}.py", f"usr/bin/{args[1]}.py")
    except Exception as e:
        print(f"[red bold]ERROR: No such file ! ({e})")
except:
    print("""
pm: a package manager for IZOS !
usage: pm <package name>
args: -s:specify an raw githubusercontent url [bold]without the filename[/bold].if not specified, use the https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/ repo.
example:
pm test
or
pm -s https://raw.githubusercontent.com/ExampleUser/ExampleRepo/ExampleBranch/ test
[red bold]Please specify a package name !
    """)