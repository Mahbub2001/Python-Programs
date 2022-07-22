# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 


def test(string):
    import re
    merged = re.split(r"([ ,]+)", string)
    return [merged[::2], merged[1::2]]
    #first return is for strings and the next is for why it was split! comma or space


s = "love Python, Programs."
print(test(s))


s = "The dance, held in the school gym, ended at midnight."
print(test(s))

s = "The colors in my studyroom are blue, green, and yellow."
print(test(s))

