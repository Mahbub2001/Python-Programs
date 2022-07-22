'''
32. Write a Python program to get the least common multiple (LCM) of two positive integers. 
'''
# Python program to find LCM of two numbers

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a % b)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 22
b = 72
print(f"LCM of {a} and {b} is {lcm(a,b)}")


