'''
26. Write a Python program to create a histogram from a given list of integers.

'''
def histogram(list1):
    for n in list1:
        for i in range(n):
            print("*",end="")
        print("\r")

histogram([2,3,10,5])