'''
#Write a program to find greatest of four numbers entered by the user

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num3

if(f1 > f2):
    print(str(f1) + " is geratest")  
else:
    print(str(f2) + " is greatest")              

'''

'''
#write a program to find out whether a student pass or fail .if it requiires total 40% and at least 33% in each subject to pass.Assume 3 subject and 
#take marks as an input from the user

subject1 = int(input("Enter the subject- 1 marks : "))
subject2 = int(input("Enter the subject- 2 marks : "))
subject3 = int(input("Enter the subject- 3 marks : "))

if(subject1 < 33 or subject2 < 33 or subject3 < 33):
    print("You are fail because you have less than 33% in this any subject")

elif((subject1 + subject2 + subject3)/3 < 40):
    print("You are fail because total percentage is less than 40")    

else:
    print("Congratulation! YOU are passed")

'''

'''
#A spame comment is defined as a text containing following keywords
#"make a lot of money","busy now","sulycrite this",
#"click this".Write the detect these spams

text = input("enter the text : \n")

spam = False

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this"):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam") 


'''

'''
#write a program to find out whether a given username contains less than 10 carracters or not

name = input("Enter your name : ")

if len(name) < 10:
    print("Yes")
else:
    print("No")
'''

'''
#name present or not in the list

names = ["turza","ruman","tonmay","mahfuz","ahmed","rahim","karim"]
name = input("Enter your name : ")

if name in names:
    print("Your name is present in the list ")
else:
    print("Your name is not present in the list")

'''

'''
#write a program to calculate the grade of a student from his marks from the following scheme:
90 - 100 -> Ex
80 - 89 -> A
70 - 79 -> B
60 - 69 -> C
50 - 59 -> D
< 50 -> F

marks = int(input("Enter your marks : "))

if marks >= 90 and marks <= 100:
    grade = "Excellent"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks <50 and marks >= 0:
    grade = "Failed"
else:
    grade = "Invalide mark"

print("Your Grade is : " + str(grade))
'''

