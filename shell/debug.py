if isroot:
    print("Debug Shell")
    while True:
        exstr = input("[red bold]#[/red bold]:")
        if exstr == "exit":
            break
        else:
            try:
                exec(exstr)
            except Exception as e:
                print(f"[blue] error:{e}")
else:
    error("Run this program as root")