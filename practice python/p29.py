'''
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

'''
x = int(input("Enter the first number : "))
y = int(input("Enter the second integer number : "))

while y != 0:
    gcd = y
    y = x % y
    x = gcd

print(f"The gcd is {gcd}")



# By Recursion

def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a % b)

x = int(input("Enter the first number : "))
y = int(input("Enter the second integer number : "))

print(f"The gcd of {x} and {y} is {gcd(x,y)}")