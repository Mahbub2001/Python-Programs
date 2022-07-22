#write a program using fucntion to find greatest of three number

def maximum(num1,num2,num3):
    if (num1 > num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(5,3000,324)
print("The maximum value is : " + str(m))

#write a python program using function to convert celcius to farenhide

def convert(cel):
    return(cel*(9/5)) + 32 

c = 70
f = convert(c)
print("FArenhide Teperature is : " + str(f))

#how do you prevent a python print() function to print a new line at the end

print("Hello", end = " ")##end = "" use kre
print("How", end = " ")
print("are", end = " ")
print("you?", end = " ") 

#a recursive finction to calcualte the sum of first natural number

def calculate(n):
    if (n == 0):
        return n
    else:
        return n + calculate(n - 1)
      
print(calculate(4))

#write a python function to remove a given word from a string and strip it at the same time

def remove_split(string,word):
    newStr = string.replace(word,"")#remove the word
    return newStr.strip()

this = "        Harry is a good boy          "
n = remove_split(this,"Harry")
print(n)

###################################################################################################################################################################################################

this = "he is a boy"
x = this.split()
print(x)
# bracket er vitore ki kisu bosale jekhane jekhaneoi carracter ta pabe sekhane sekhane split korbe
#example:

text = 'geeks for geeks'
  
# Splits at space
print(text.split())
  
word = 'geeks, for, geeks'
  
# Splits at ','
print(word.split(','))
  
word = 'geeks:for:geeks'
  
# Splitting at ':'
print(word.split(':'))
  
word = 'CatBatSatFatOr'
  
# Splitting at t
print(word.split('t'))

##########################################################################################################################################################################################################