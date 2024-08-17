import platform
import subprocess

if platform.system() == 'Windows':
    subprocess.check_call(["pip"], ["install"], ["-r"], ["win-requirements.txt"])
else:
    subprocess.check_call(["pip"], ["install"], ["-r", ["linux-mac-requirements.txt"]])