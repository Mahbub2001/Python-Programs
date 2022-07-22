import os

oldname = "p18.txt"
newname = "renamed_by_python.txt"

with open(oldname,"r")as f:
    content = f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)#####