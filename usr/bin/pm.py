import sys
import urllib.request
sys.path.append("../lib")
import base
from base import print
try:
    arg = shell[1]
    try:
        if shell[1] == "-s" or shell[1][1] == "-":
            print(f"Saving {shell[3]}.py using custom repo {shell[2]}..")
            urllib.request.urlretrieve(f"{shell[2]}{shell[3]}.py", f"usr/bin/{shell[3]}.py")
        else:
            print(f"Saving {shell[1]}...")
            urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/{shell[1]}.py", f"usr/bin/{shell[1]}.py")
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