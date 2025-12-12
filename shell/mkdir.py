#### makedir utility
import os
helpstr = """
[bold blue]makedir Utility[/bold blue]
Usage: [bold]mkdir \[required: dir name][/bold]
[bold]'dir name'[/bold]: the directory name.
"""
if len(commandargs) == 1:
    print(helpstr)
else:
    try:
        if commandargs[1][0] == "/":
            os.mkdir(f".{commandargs[1]}")
        else:
            os.mkdir(f"{dir}/{commandargs[1]}")
    except Exception as e:
        print(e, " ", "An error occured ! Either the directory is already present, or the path is incorrect !")