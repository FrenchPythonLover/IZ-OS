#### touch utility

if len(commandargs) == 1:
    print("Error !")
else:
    with open(f"{dir}{commandargs[1]}","a+") as touched:
        pass
    