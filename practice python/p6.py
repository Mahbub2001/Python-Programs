'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

values = input("Input some seperate numbers by comma : ")

list = values.split(",")#split(" jeti thakle split ")
tuple = tuple(list)

print(f"List  : {list}" )
print(f"Tuple : {tuple}")