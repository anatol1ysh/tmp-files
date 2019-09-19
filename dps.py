# user1@buntu:~$ cat script_/dps.py
import os
import time

while True:
    os.system('clear')
    os.system('docker ps -a')
    print '\n'
    os.system('netstat -nultp')
    time.sleep(2)
