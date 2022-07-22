'''
23. Write a Python program to get the n 
(non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
'''

def copy(a,n):
    st = ""
    if len(a) <= 2:
        for i in range(n):
            st = st + a
        return st
    else:
        newstr = a[:2]

    for i in range(n):
        st = st + newstr
    return st

a = input("Enter the string : ")
n = int(input("enter the ammount of copy : "))
print(copy(a,n))