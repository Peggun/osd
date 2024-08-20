import platform
import subprocess

# This is just for people on different OS'

if platform.system() == 'Windows':
    subprocess.run(["pip", "install", "-r", "win-requirements.txt"])
else:
    subprocess.run(["pip", "install", "-r", "linux-mac-requirements.txt"])