# Cat utility
helpstr = """
[bold blue]Cat utility: Display a file's content[/bold blue]
"""
if len(commandargs) == 1:
    print(helpstr)
else:
    ftc = commandargs[1] # 'ftc' for "File to cat".
    try:
        with open(dir + ftc,"r") as file:
            print(file.read())
    except:
        print("File not found (if used absolute path use 'catabsolute')")