'''
#write a program to print multiplication table of a given number using for loop
num = int(input("enter the number : "))

for i in range(1,11):
    #print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num} X {i} = {num*i}")#fstrings er sahajje esily solve 
'''


'''
#write a program to greet all the person names stored in a list l1 and which starts with S
#  l1 = ["Harry","Sohan","Sachin","Rahul"]

l1 = ["Harry","Sohan","Sachin","Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello "+ name)

'''

'''
#attemp problem 1 with while loop

num = int(input("enter the number : "))
i = 1

while i <=10:
    print(f"{num} X {i} = {num*i}")
    i+=1

'''

'''
#write a program to find whether a given number is prime or not

num = int(input("enter the nubmer that you want : "))

prime = True

for i in range(2,num):
    if (num % i == 0):
        prime = False
        break

if prime:
    print("This number is prime")
else:
    print("This number is not a prime number")

'''

'''
#to find the sum of first n natural numbers using while loop

n = int(input("Enter the number of natural number : "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i+=1

print("The sum is " + str(sum))

'''


'''
#calculate the factorial of a given number using for loop 

n = int(input("Enter the number that you want : "))
fact = 1
for i in range(1,n+1):
    fact  = fact*i

print(fact)

'''

'''
#print star pattern 

n = int(input("Enter the number : "))

for i in range(1,n+1):
    print(i* '*')


'''

'''
#print star pattern 
    * 
   * *
  * * *
 * * * *
* * * * *
'''

n = int(input("Enter the number : "))

k = n - 1 # number of spaces

for i in range(0,n):# outer loop to handle number of rows
    for j in range(0,k):    # inner loop to handle number spaces
        print(end=" ")
    k = k - 1      # decrementing k after each loop
    for l in range(0,i + 1):      # inner loop to handle number of columns
        print("* ",end="")
    print("\r")    
    

