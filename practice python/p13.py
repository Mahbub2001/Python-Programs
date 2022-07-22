'''
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

'''
from datetime import date

year1 = int(input("Enter the year : "))
month1 = int(input("Enter the month : "))
day1 = int(input("Enter the day1 : "))

year2 = int(input("Enter the year2 : "))
month2 = int(input("Enter the month2 : "))
day2 = int(input("Enter the day2 : "))

from_date = date(year1,month1,day1)
to_date = date(year2,month2,day2)

difference = to_date - from_date

print(difference.days)