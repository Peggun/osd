import subprocess
import time
import sys
import platform

# Runs the tests as you need multiple threads. One to run the server, and one to run pytest.

if platform.system() == "Windows":

    server_process = subprocess.Popen(["py", "run.py"])

    time.sleep(5)

    result = subprocess.run(["pytest"], capture_output=True, text=True)
    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        sys.exit(result.returncode)

    server_process.terminate()
    sys.exit()

else:
    server_process = subprocess.Popen(["python", "run.py"])

    time.sleep(5)

    result = subprocess.run(["pytest"], capture_output=True, text=True)

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        sys.exit(result.returncode)

    server_process.terminate()
    sys.exit()
