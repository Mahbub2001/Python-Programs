'''
25. Write a Python program to check whether a specified value is contained in a group of values. 
'''

def check(list1,num):
    for number in list1:
        if number == num:
            return True
    return False

list1 = [4,5,6,3,7,2]
print(check(list1,100))
print(check(list1,4))


