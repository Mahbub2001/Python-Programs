'''
Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).

'''

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
z = int(input("Enter the value of z : "))
t = int(input("Enter the value of t : "))

s = sum([x,y,z,t])
print(f"\nSum of the container : {s}\n")

s = sum((x,y,z,t))
print(f"Sum of the container : {s}\n")


### set er khetre jehetu duplicate value ############# 
s = sum({x,y,z,t})
print(f"Sum of the container : {s}\n")
### set er khetre jehetu duplicate value #############
