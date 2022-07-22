
# while loop 

# i = 0

# while i < 10 :
#     print("Yes " + str(i))
#     i+=1

# print("Done") 

fruits = ['Banana','watermilon','Graps','Mangoes']

i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1




#for loop

fruits = ['Banana','watermilon','Graps','Mangoes']

for item in fruits:
    print(item)



'''
#range function:

for i in range(8):# 0 theke 8 ta print hbe
    print(i)

for i in range(1,8):# 1 theke 8 er ag prjnto
    print(i)

for i in range(1,8,2):
    print(i)

'''
'''

#for with else

for i in range(10):
    print(i)

else:# jkhn loop end hbe tkhn else execute hbe 
    print("This is inside else of for")

'''

'''
#break staetment:

for i in range(10):
    print(i)
    if i == 5:
        break 
else:
    print("This is inside else of for")

'''
'''
#Continue :
    
for i in range(10):
    if i == 5 :
        continue
    print(i)

'''
'''
#pass statement

i = 4
if i > 0:
    pass
print("Tonmay is a good boy")  

'''