import subprocess
from time import time as t

proc = subprocess.Popen(args=['echo', 'Hello world from py subprocess'], stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()

print(out.decode('utf-8'))

def run_sleep(period):
    process = subprocess.Popen(args=['Start-Sleep', str(period)], stdout=subprocess.PIPE, shell=True)
    return process

start = t()
processes = []
for i in range(10):
    process = run_sleep(0.1)
    processes.append(process)

for process in processes:
    process.communicate()
end = t()

print(f'Finished in {end - start}')