'''
Write a Python program to add two objects if both objects are an integer type.

'''

def calculate(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        return "Input Must Be Integer"
    return a + b


a = input("Enter the first number : ")
b = input("Enter the second number : ")

c = calculate(a,b)

print(f"The sum of {a} and {b} : {c}")


############################################################

#isinstance(OBJECT,TYPE)