import sys
import os
sys.path.append("../lib/")
import base
helpstr = """
[blue bold underlined]HelloPy v1: An IZOS utility[/blue bold underlined]
[green]Commands:[/green]
-v or --version: display HelloPy version
--izos-version: display IZOS version
--lsbin or --list-bin:list the programs on the [bold]/usr/bin/[/bold] directory
"""

try:
    arg = args[1]
    if arg == "-h" or arg == "--help":
        print(helpstr)
    if arg == "-v" or arg == "--version":
        print("[blue]HellPy v1.1")
    if arg == "--izos-version":
        print(version)
    if arg == "--lsbin" or arg == "--list-bin":
        print(os.listdir("usr/bin/"))
except:
    print(helpstr + "[red]Error: Please specify a argument !")