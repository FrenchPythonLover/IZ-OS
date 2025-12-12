## Update check
print("Update Checking...")
from urllib.request import urlretrieve
from infosys import version
officialrepo = "https://raw.githubusercontent.com/FrenchPythonLover/IZ-OS/refs/heads/main/version"
urlretrieve(f"{officialrepo}", f"./shell/rc/version")
with open("./shell/rc/version","r") as verfile:
    content = verfile.read().strip()
    remote_version = content.split()[0] if content else ""
    if remote_version != version:
        
        exit("print('The latest version is NOT installed. Please check github.')")
    else:
        print("Latest version is installed !")
        os.remove("./shell/rc/version")
        