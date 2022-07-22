'''
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
'''
feet = float(input("Enter the distance in feet : "))

inches = feet * 12
yards = feet / 3.0
miles = feet / 5280.0

print(f"The inches will be {inches}")
print(f"The yards will be {yards}")
print(f"The miles will be {miles}")