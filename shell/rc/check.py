import os
info("Starting PyCheck v1..;")
print("Scanning...")
dirs = ["home","usr","usr/bin","usr/lib","lib","shell","root","shell/rc"] # in theory, if shell/rc is missing check.py cannot start. but i just want to add some chars.
for checkindex in range(len(dirs)):
    print(f"Checking directory {dirs[checkindex]}")
    try:
        os.listdir(f"./{dirs[checkindex]}")
        ok(f"Directory {dirs[checkindex]} is present !")
    except:
        error(f"The directory {dirs[checkindex]} is missing. Cannot start.")
        exit()
ok("Finished !")