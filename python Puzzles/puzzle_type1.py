# Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.

def testing(number):
    return number % 34 == 4 and number > 4**4

print(testing(922))
print(testing(914))
print(testing(1004))