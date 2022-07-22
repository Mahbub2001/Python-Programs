'''
Write a Python program to get the current value of the recursion limit
'''

import sys
print("Call sys.getrecursionlimit() to get the current recursion limit:")
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)
print("\nCall sys.setrecursionlimit(n) to change the recursion limit to n operations:")
sys.setrecursionlimit(1001)
new_recursion_limit = sys.getrecursionlimit()
print(new_recursion_limit)



