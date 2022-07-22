'''
 Write a python program to access environment variables
'''

import os
for data in os.environ:
   print(data)
   print('-'*15)
   print(os.environ[data])
   print('='*30)