marks = [95, 98, 97, "maths"]
# print(marks)
# print(marks[0])
# print(marks[-1])### - dile pison theke start hbe 

# print(marks[0:2])## eto theke eto 

for score in marks :
    print(score)

# marks.append(99)# sese add kora 
# print(marks)   

# marks.insert(0,99)##jekono jaygay add korar jnno 
# print(marks)  

# print(99 in marks)## checking exist or not
# print(1000 in marks)## checking exist or not

# print(len(marks))##length

# i = 0
# while i < len(marks) :
#     print(marks[i])
#     i +=1

# marks.clear()#puro list khali korar jnno
# print(marks)

# students = ["tomy","tonmay","mahfuz","ahmed","mahbub"]

# for student in students:
#     if student =="mahfuz":
#         break
#     print(student)    

# for student in students:
#     if student =="mahfuz":
#         continue;
#     print(student)      


#####################################################

####ei poddhoti te space dile kaj hbe na....enter diye diye nite hbe
# marks=[]
# n = int(input("Enter the number of elements : "))

# for i in range(0,n):
#     element = input()
#     marks.append(element)

# print(marks)    


####################################################number of elements###ei poddhoti te space diye diye krte hbe..enter dile exit hye jabe
# n = int(input("Enter number of elements : "))

# # Below line read inputs from user using map() function
# a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

# print("\nList is - ", a)
#################################################################################################extra#################################################################
# lst = [] 
# n = int(input("Enter number of elements : ")) 
  
# for i in range(0, n): 
#     ele = [input(), int(input())] 
#     lst.append(ele) 
      
# print(lst)
#################################################################################################extra#################################################################


##########################slicing##################
# marks = []
# n = int(input("Enter the enumber of elements : \n"))

# for i in range(0,n):
#     element = int(input())
#     marks.append(element)

# print(marks)  
# print(marks[0:2])#slicing
# print(marks[:-3])

#####################################################################################
                                      #Method

marks = [23,9,11,90,44]
print(marks)
# marks.sort()##for sorting
# print(marks)
# marks.reverse()##reverse krar jnno
# print(marks)
# marks.append(1000)##append krar jnno
# print(marks)
# marks.insert(1,544)##kthay insert krar jnno
# print(marks)
# marks.pop(2)###index e remove krar jnno
# print(marks)
marks.remove(11)##specific value remove
print(marks)