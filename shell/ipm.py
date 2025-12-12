#### IZOS Package Manager
## TODO: Faire un système de parse json pour déterminer si lib ou bin !
from urllib.request import urlretrieve
import tmp
from os import remove
officialrepo = "https://raw.githubusercontent.com/FrenchPythonLover/IZOSAPPS/refs/heads/main/"
helpmsg="""
[blue]ipm - A package manager for IZOS[/blue]
Usage: [code]ipm \[options] program[/code]
Options :
[code]install[/code]: install a program
[code]rm[/code]: remove a program
[code]rmall[/code]: remove [bold]all[/bold] programs. Do not need another argument.
"""
url = ""
if not isroot:
    print("[red]You need superuser permissions to run ipm[/red]")
else:
    try:
        option = commandargs[1]
        
        if len(commandargs) <= 2:
            
            if len(commandargs) == 1:
                print(f"{helpmsg} [red]Please specify an argument or option not recognised")
            if option == "rmall":
                print("Working on this. for the moment just reset the installation")
            else:
                print(f"{helpmsg} [red]Please specify an argument or option not recognised")
        else:
            prgm = commandargs[2]
            match option:
                
                case "install":
                    try:
                        urlretrieve(f"{officialrepo}{prgm}.py", f"./usr/bin/{prgm}.py")
                        print(f"[green bold]Installed {prgm} !")
                    except:
                        print(f"[red bold]An error happenend installing {prgm}")
                case "rm":
                    try:
                        remove(f"./usr/bin/{prgm}.py")
                        print(f"[green bold]Removed {prgm} !")
                    except:
                        print(f"[red bold]An error happened removing {prgm}")
                case _:
                    print(helpmsg)

        # if fn == "rm":
        #     import os
        #     os.remove(f"apps/{commandargs[2]}.py")
        # else:
            
    except:
        print(helpmsg)
# urlretrieve(f"{officialrepo}{fn}.py", f"apps/{fn}.py")