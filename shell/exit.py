if isroot:
    with open("./shell/su.py","r") as su:
        exec(su.read())
else:
    exit()