# CD Utility
tempdirls = commandargs[1]
try:
    
    tempdir = f"{tempdirls}/"
    if tempdir == "//":
        print("[yellow bold]Warning: Please refer to root as [green]./[/green] and not [red]/[/red]")
        a = os.listdir(tempdirls)
        dir = f"./" # <-- the / keeps the system from breaking
    elif tempdir[0] == "/" and len(tempdir) != 2:
        print("[red bold]Error: Please refer to root as [green]./[/green]")
        print("Operation aborted.")
    else:
        a = os.listdir(tempdirls)
        dir = f"{tempdirls}/"
    a=0
except:
    print("[red bold]The specified directory does not exists ![/red bold]")