'''
#write a program to make a copy of a text file 'this.txt
'''

with open("this.txt","r") as f:
    content = f.read()
with open("copy.txt","w") as f:
    f.write(content)

