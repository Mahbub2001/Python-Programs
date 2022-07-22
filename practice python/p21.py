'''
22. Write a Python program to count the number 4 in a given list.
'''
list1 = [5,4,6,4,8,3,4,10]
print(list1.count(4))

#or,
list1 = [5,4,6,4,8,3,4,10]

count = 0
for num in list1:
    if num == 4:
        count+=1

print(count)
