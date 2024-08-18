import platform
import subprocess

if platform.system() == 'Windows':
    subprocess.run(["pip", "install", "-r", "win-requirements.txt"])
else:
    subprocess.run(["pip", "install", "-r", "linux-mac-requirements.txt"])