'''
Write a Python program to get the size of an object in bytes.
'''

import sys
str1 = "one"
str2 = "four"
str3 = "three"
x = 0
y = 112
z = 122.56

print("Size of ",str1,"=",str(sys.getsizeof(str1))+ " bytes")
print("\n")

print("Size of ",str2,"=",str(sys.getsizeof(str2))+ " bytes")
print("\n")

print("Size of ",str3,"=",str(sys.getsizeof(str3))+ " bytes")
print("\n")

print("Size of",x,"=",str(sys.getsizeof(x))+ " bytes")
print("\n")

print("Size of" ,y,"="+str(sys.getsizeof(y))+ " bytes")
print("\n")

L = [1, 2, 3, 'Red', 'Black']
print("Size of",L,"=",sys.getsizeof(L)," bytes")
print("\n")

T = ("Red", [8, 4, 6], (1, 2, 3))
print("Size of",T,"=",sys.getsizeof(T)," bytes")
print("\n")

S = {'apple', 'orange', 'apple', 'pear'}
print("Size of",S,"=",sys.getsizeof(S)," bytes")
print("\n")

D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
print("Size of",D,"=",sys.getsizeof(S)," bytes")
print("\n")
