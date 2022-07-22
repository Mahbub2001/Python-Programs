'''
19. Write a Python program to get a new string from a given string 
where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
'''

def fun1(a):
    if len(a) >= 2 and a[:2] == "Is":
        return a
    else:
        return "Is " + a

a = input("Enter the string : ")

newstr = fun1(a)
print(newstr)