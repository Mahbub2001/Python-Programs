'''
69. Write a Python program to sort three integers without using conditional statements and loops. 

'''

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))

a1 = min(x,y,z)# min number min() finction diye ber kra jay
a3 = max(x,y,z)# max number max() function diye ber kra jay
a2 = (x + y + z) - a1 - a3

print(f"Numbers in sorted way : {a1,a2,a3}")


#or

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))

list1 = [x,y,z]

print(list1.sort())
