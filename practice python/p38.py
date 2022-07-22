'''
45. Write a Python program to call an external command.
'''

from subprocess import call
call(["ls", "-l"])

import os
print(os.system('ls -l'))