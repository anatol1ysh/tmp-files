import datetime
import random
import os
import time

file_name = "out_mock_py_1.log"
f = open(file_name, "a+")

hub_state = ["GREEN", "YELLOW", "RED"]
hub_id = [100010000, 100010011, 100010022, 100010033, 100010044, 100010055, 100010066, 100010077, 100010088, 100010099]

main_count = 0
file_reset_counter = 0
print("Write some payload to file: " + file_name + "\n")
#for i in list(range(10000)):
while True:
    cnt = 0
    main_count += 1
    time.sleep(1)
    print("Done " + str(main_count) + "\n")
    for item in hub_id:
        cnt += 1
        file_reset_counter += 1

        # str(datetime.datetime.now().strftime("%Y.%m.%d %H:%M "))
        # f.writelines(" Hub_ID: " + str(item) + " Count_resp: "+ str(random.randrange(511, 2047)) + " State: " + hub_state[random.randrange(0, 4)] + " Count: " + str(cnt) + "  Signal_lvl: " + str(random.randrange(10, 100)) + "%  Battery_lvl: " + str(random.randrange(10, 100)) + "% \n")
        f.writelines(str(item) + " " 
            + str(random.randrange(1000, 1500)) + " "
            + hub_state[random.randrange(0, 3)] + " " 
            + str(cnt) + " " 
            + str(random.randrange(40, 80)) + "dB " 
            + str(random.randrange(10, 100)) + "%\n")
        if main_count == 9999:
            main_count = 0
        
f.close()

""" if file_reset_counter == 9999:
    print('Reset output file: ' + file_name)
    os.system('ls -all -h')
    os.system('echo "" > ~/script_/out_mock_py_1.log')
    #time.sleep(10)
    print('Pause 10 second!')
    for i in list(range(10)):
        sleep(1)
        print('Pause ' + str(10 - i) + ' sec.')
    file_reset_counter = 0
    print("Write some payload to file: " + file_name + " after reset.\n")
"""