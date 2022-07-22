'''
18. Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum.
'''



def sum1(x,y,z):

    sum = x + y + z

    if (x == y == z):
        sum = sum*3
    return sum

print(sum1(56,5,25))
print(sum1(11,11,11))
        