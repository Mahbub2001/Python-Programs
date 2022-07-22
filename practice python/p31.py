'''
34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''

def calculateSum(a,b):
    sum1 = a + b
    if(sum1 >= 15 and sum1 <= 20):
        return 20
    else:
        return sum1


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

c = calculateSum(a,b) 

print(f"The sum is {c}")