'''
Write a Python program to swap two variables.
'''

a = int(input("Enter the value of first number : "))
b = int(input("Enter the value of second number : "))

a,b = b,a
print(f"After swaping {a,b}")
