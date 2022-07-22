'''
Write a Python program to sum of the first n positive integers.
'''

a = int(input("Enter the range : "))
sum1 = 0
for i in range(1,a+1):
    sum1 = sum1 + i

print(f"The sum is {sum1}")