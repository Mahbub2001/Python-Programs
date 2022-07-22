# Write a Python program to check a given list of integers where the sum of the first i integers is i.

def checking(lis):
    return all(sum(lis[:i]) == i for i in range(len(lis)))


list1 = [0,3,2,2,3]
print(checking(list1))

list1 = [1,1,1,1,1,1]
print(checking(list1))
