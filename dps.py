import os
import time

os.system('netstat -nultp | grep tcp6')
for i in list(range(100)):
    os.system('docker stats --no-stream')
    print '\n'
    #os.system('clear')
