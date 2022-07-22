'''
repeat qs 4 for a list of words to be consord
'''
words = ["donkey","gadha","pagol"]

with open("p12.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"2489&%")
    with open("p12.txt","w") as f:
        f.write(content)
