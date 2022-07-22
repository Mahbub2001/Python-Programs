'''
Write a Python program to get file creation and modification date/times.
'''

import os.path, time
print(f"Last modified: %s" % time.ctime(os.path.getmtime("p45.py")))
print("Created: %s" % time.ctime(os.path.getctime("p45.py")))


