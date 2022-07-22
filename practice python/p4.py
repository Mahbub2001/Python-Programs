'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

from math import pi

r = float(input("Enter the radius : "))
area = float(pi*(r*r))

print(f"The area of the circle is =  {area} ")