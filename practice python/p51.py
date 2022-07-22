'''
 Write a Python program to convert all units of time into seconds
'''

days = int(input("Input days that you want : ")) * 3600 * 24
hours = int(input("Input hours that you want : ")) * 3600
minutes = int(input("Input minutes that you want : ")) * 60
seconds = int(input("Input seconds that you want : "))

time = days + hours + minutes + seconds

print(f"The seconds {time}")
