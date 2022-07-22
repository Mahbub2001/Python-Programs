'''
Write a Python program to get the size of a file.
'''

# import os
# file_size = os.stat("p19.py")
# print("\nThe size of abc.txt is :",file_size.st_size,"Bytes")


import os
file_size = os.stat("p40.py")
print(f"The size of p19.py is : {file_size.st_size} Bytes")