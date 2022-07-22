'''
a file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file
'''

with open("p11.txt","r") as f:
    content = f.read()

content = content.replace("donkey","2489&%")

with open("p11.txt","w") as f:
    f.write(content)



