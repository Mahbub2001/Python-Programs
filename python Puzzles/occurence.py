# Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. 



def testing(numbers):
    return numbers.count(19) == 2 and numbers.count(5) >= 3

list1 = [19, 19, 15, 5, 3, 5, 5, 2]
print(testing(list1))

list2 = [19, 15, 5, 3, 5, 5, 2]
print(testing(list2))