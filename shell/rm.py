import os
blocklist = ["lib","root","home","apps","shell"]
if len(commandargs) == 1:
    print("Please specify an argument")
else:
    try:
        os.remove(f"{dir}{commandargs[1]}")
        
    except:
        print("file does not exist")