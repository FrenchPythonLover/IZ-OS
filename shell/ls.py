# LS utility v1
# TODO: faire un parsing arguments
helpstr = """
[bold blue]LS Utility[/bold blue]
Usage: [bold]ls \[optional: [cyan]path[/cyan]][/bold]
list the current directory, or the [bold]path[/bold] argument can specify another dir to list.
"""
lsout = os.listdir(dir)
if len(commandargs) != 1:
    if commandargs[1] == "--help" or commandargs[1] == "-h":
        print(helpstr)
    else:
        try:
            lsout = os.listdir(commandargs[1])
            print(' '.join(map(str, lsout)))
        except:
            print("[bold red]error: The specified directory does not exist !")
else:
    try:
        lsout = os.listdir(dir)
        print(' '.join(map(str, lsout)))
    except:
        print("[bold red]An unspecified error has occured")