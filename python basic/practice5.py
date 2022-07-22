#Write a program to creat a dictionary of english words with values as their bangla translation provide user with an option to look it up

# myDictionary = {
#     "Horse" : "Ghora",
#     "book" : "Boi",
#     "Pen" : "kolom"
# }

# print("Options are : ",myDictionary.keys())
# a = input("Enter the english word : ")
# #print("The meaning of your word is : ",myDictionary[a])

# #Below line will not throw error
# print("The meaning of your word is : ",myDictionary.get(a))


#Write a program to input eight number form the user and display all the unique numbers

# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))
# num3 = int(input("Enter Number 3 : "))
# num4 = int(input("Enter Number 4 : "))
# num5 = int(input("Enter Number 5 : "))
# num6 = int(input("Enter Number 6 : "))
# num7 = int(input("Enter Number 7 : "))
# num8 = int(input("Enter Number 8 : "))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)

#Can we have a set with 18(int) and "18"(str) as a value in it?

# s = {18,"18"}
# print(len(s))

#jehetu 1 ta string 1 ta integer ..jar karone python duto k alada alada dhrobe.. alada alada vabei print krbe..unique hisebe count krbe

'''
#What will be the lenght of following set?
s = set()
s.add(20)
s.add((20.0))
s.add("20")
'''

# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")

# print(len(s))

#float ar integer ekei nibe..ejnno length 2 hbe


'''
s = {}
what is th type of s?

er type ta dictioanry hbe..set hbe na
'''

'''
Creat an empty dictionary allow 4 friends to enter their favorite language as values and use as their names. Assume that the names are unique

mydict ={}

a = input("Enter your favorite language Turza : \n")
b = input("Enter your favorite language Mahbub : \n")
c = input("Enter your favorite language Tonmay : \n")
d = input("Enter your favorite language Mahfuz : \n")

mydict["Turza"] = a
mydict["Mahbub"] = b
mydict["Tonmay"] =c
mydict["Mahfuz"] = d

print(mydict)
'''

'''
If names pf 2 friends are same; what will to the problem program 6 :

mydict ={}

a = input("Enter your favorite language Turza : \n")
b = input("Enter your favorite language Mahbub : \n")
c = input("Enter your favorite language Tonmay : \n")
d = input("Enter your favorite language Mahfuz : \n")

mydict["Turza"] = a
mydict["Mahbub"] = b
mydict["Turza"] =c
mydict["Mahfuz"] = d

print(mydict)

porer turza ta execute hye jabe..ager tar sathe replace hye jabe

'''

'''
if languages of two friends are same what will happen to the program in that problem

kono somossa hbe na....values unique houya joruri na . keys ta unique hte hbe
'''
'''
can you chaneg the values inside a list which is contain in set S
S= {8,7,12,"Harry",[1,2]}

error hbe.tuple o chlbe na
'''
