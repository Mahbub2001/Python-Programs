# Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list. 

def testing(numbers):
    return len(numbers) == 8 and numbers.count(numbers[4]) == 3

nums = [19,19,15,5,5,5,1,2]
print(testing(nums))

nums = [19,15,5,7,5,5,2]
print(testing(nums))

nums = [11,12,14,13,14,13,15,14]
print(testing(nums))

nums = [19,15,11,7,5,6,2]
print(testing(nums))