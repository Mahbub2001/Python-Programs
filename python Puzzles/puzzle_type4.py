'''
Write a Python program to test a list of one hundred integers 
between 0 and 999, which all differ by ten from one another.
Return true or false.
'''

def checking(list1):
    return all(i in range(1000) and abs(i - j) >= 10 for i in list1 for j in list1 if i != j) and len(set(list1)) == 100


nums = list(range(0, 1000, 10))
print(nums)
print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
print(checking(nums))

print("\n")
nums = list(range(0, 1000, 20))
print(nums)
print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
print(checking(nums))
