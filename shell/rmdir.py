import os
blocklist = ["lib","root","home","apps","shell"]
if len(commandargs) == 1:
    print("Please specify an argument")
else:
    try:
        if commandargs[1] in blocklist and not isroot and dir == "./":
            print("[red]you do not have permission to delete this directory")
        elif commandargs[1] in blocklist and isroot and dir == "./":
            if input("Are you sure you want to delete a system directory ? (y/n)").lower() == "y":
                os.rmdir(f"{dir}{commandargs[1]}")
            else:
                print("Operation aborted")
        else:
            os.rmdir(f"{dir}{commandargs[1]}")
        
    except Exception as e:
        print(e,"An error occured. maybe the dir isn't empty")