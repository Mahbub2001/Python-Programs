'''
Write a Python program to get the copyright information and write Copyright information in Python code.

'''

import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()


'''
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
'''
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))



'''
Write a Python program to test whether the system is a big-endian platform or little-endian platform.
'''


import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()