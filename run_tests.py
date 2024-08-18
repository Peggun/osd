import subprocess
import time

server_process = subprocess.Popen(['py', 'run.py'])

time.sleep(5)

result = subprocess.run(['pytest'], capture_output=True, text=True)

print(result.stdout)

server_process.terminate()