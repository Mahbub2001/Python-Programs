# f = open("sample.txt","r")#by default this mode is r 
# data = f.read(5)
# print(data)
# f.close()


# f = open("sample.txt","r")
# data = f.readline()#line print korar jnno
# print(data)
# data = f.readline()#joto ber lekha hbe next line ta kre print krte thakbe
# print(data)
# f.close()


# f = open("another.txt","w")
# f.write("Please write this to the file")
# f.close()

# f = open("another.txt","a")
# f.write("\nmy name is mahbub ahmed turza")
# f.close()

with open("another.txt","r") as f:
    a = f.read()

with open("another.txt","w") as f:
    a = f.write("my name is mahbub ahmed turza")

print(a)