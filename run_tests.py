import subprocess
import time
import platform

if platform.system() == 'Windows':

    server_process = subprocess.Popen(['py', 'run.py'])

    time.sleep(5)

    result = subprocess.run(['pytest'], capture_output=True, text=True)

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    server_process.terminate()

else:
    server_process = subprocess.Popen(['python', 'run.py'])

    time.sleep(5)

    result = subprocess.run(['pytest'], capture_output=True, text=True)

    print(result.stdout)

    server_process.terminate()