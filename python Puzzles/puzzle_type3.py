# Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.

def check(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

str11 = ["a","abb","sfs", "oo", "de", "sfde"]
print(check(str11))

str11 = ["a","abb","sfs", "oo", "ee", "sfde"]
print(check(str11))


def check(str1):
    return str1[len(str1) - 2] in str1[len(str1) - 1] and str1[len(str1) - 2]