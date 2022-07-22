#C = P(1+r)^n2

'''
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

'''

principal = float(input("Enter the main balance : "))
r = float(input("enter the interest rate : "))
years = int(input("Enter the year : "))

future_value = principal*((1+(0.01*r)) ** years)

print(round(future_value,2))