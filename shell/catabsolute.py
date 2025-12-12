# Cat utility
if commandargs[1][0] == "/":
    ftc = f".{commandargs[1]}"
else:
    ftc = commandargs[1] # 'ftc' for "File to cat".
try:
    with open(ftc,"r") as file:
        print(file.read())
except:
    print("File not found or not using absolute path.")