'''
27. Write a Python program to concatenate all elements in a list into a string and return it.
'''
def convert1(list1):
    string = ''
    for elements in list1:
        string = string + str(elements)
    return string

print(f"The string is : {convert1([1,5,12,2])}")