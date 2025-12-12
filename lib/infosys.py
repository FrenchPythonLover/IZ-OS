#### A file containing info about the system itself

# info version
major = 1 # Version number
minor = 0
patch = 0
version = f"{str(major)}.{str(minor)}.{str(patch)}"
vertype = "release" # Release Type
# Other
import sys # For Device/Python Related info
pyversion = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"