'''
Write a Python program to get the system time.
Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
'''


import time

print(time.ctime())


# import osWrite a Python program to clear the screen or terminal.

# import os
# import time
# # for windows
# # os.system('cls')
# os.system("ls")
# time.sleep(2)
# # Ubuntu version 10.10
# os.system('clear')


# Write a Python program to get the name of the host on which the routine is running.

import socket
host_name = socket.gethostname()
print("Host name:", host_name)

