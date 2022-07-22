'''

Write a Python program to calculate sum of digits of a number.

'''

def getSum(n):
    sum = 0

    for digit in str(n):
        sum += int(digit)
                                          
    return sum

n = int(input("Enter the value of n : "))

print(getSum(n))

