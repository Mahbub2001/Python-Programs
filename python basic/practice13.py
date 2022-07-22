'''
write a program to mine a log file and find out whether it contains python

'''
with open("log.txt","r") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")


#content.lower() eti lekhar karon holo puro file take lower kre find kora jate kre capital thakleo seti k khuje pay..nahle jehetu case sensitive khuje pabe capital and small lettter er jnno
