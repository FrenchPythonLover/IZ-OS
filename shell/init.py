### Default init system
## Copyright 2025 IZOS 
ok("Init system running")
info("Detecting what to run...")
sys.path.append("./shell")
ok("appended ./shell")
import rclocal

ok("Imported rclocal.py")
if rclocal.rc:
    ok("rc is here")


info("loading every init program...")
for i in range(len(rclocal.rc)):
    with open(rclocal.rc[i],"r") as file:
        exec(file.read())
        ok(f"executed program number {i}")
ok("Finished init !")
