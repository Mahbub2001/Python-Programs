'''
#write a program to read the text from a given file 'poems.txt' and find out whether it contnains the word ' twinkle'
'''

with open("poems.txt","r") as f:
    a = f.read()

if 'twinkle' in a:
    print("twickle is present")
else:
    print("twinkle is not present")
