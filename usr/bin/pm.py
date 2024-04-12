import sys
import urllib.request
sys.path.append("../lib")
import base
from base import print
try:
    print(f"Saving {shell[1]}.py...")
    try:
        urllib.request.urlretrieve(f"https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/main/{shell[1]}.py", f"usr/bin/{shell[1]}.py")
    except Exception as e:
        print("[red bold]ERROR: No such file ! (Invalid package name)")
        print(e)
except:
    print("""
pm: a package manager for IZOS !
usage: pm <package name>
example:
pm test
[red bold]Please specify a package name !
    """)