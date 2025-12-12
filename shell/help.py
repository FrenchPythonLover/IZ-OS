## Simple Help program for IZOS
#(Prints a formatted 'cmdlist' string)
## See api doc for string cmdlist
## Then prints the apps/bin
print("[bold]Base[/bold] shell commands:")
for i in range(len(cmdlist)):
    print(cmdlist[i].replace(".py",""))

print("[bold]User installed[/bold] programs:")
appsfiles = next(os.walk("./usr/bin/"), (None, None ,[]))[2] # WTF++
for i in range(len(appsfiles)):
    print(appsfiles[i].replace(".py",""))
    