'''
29. Write a Python program to print out a set containing all the colors 
from color_list_1 which are not present in color_list_2
'''

list1 = ["black","white","red"]
list2 = ["red","green"]

list1 = set(["black","white","red"])
list2 = set(["red","green"])#convert list into set 

print("Difference of color list1 and color list 2")
print(list1.difference(list2))

print("Difference of color list2 and color list1")
print(list2.difference(list1))

###########################################################

#Using the er jesb.difference(er kase nai) function