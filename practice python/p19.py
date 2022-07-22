'''
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''

def copy(a,n):
    st = ""

    for i in range(n):
        st = st + a
    return st


a = input("Enter the string : ")
n = int(input("Enter the ammount of copy : "))
print(copy(a,n))