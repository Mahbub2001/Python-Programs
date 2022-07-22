'''
Write a Python program to calculate the hypotenuse of a right angled triangle
'''

from math import sqrt

length = float(input("Enter the lenght of the traingle : "))
base = float(input("Enter the base of the traingle : "))

hypotenuse = sqrt((length ** 2) + (base ** 2))

print(f"The hypotenuse of the traingle is {hypotenuse}")