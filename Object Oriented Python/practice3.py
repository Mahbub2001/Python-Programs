'''
creat a class with a class attribute a; creat an an object from it and set a directly using object a = 0.
Does this change the class attribute
'''

class Sample:
    a = "Turza"

obj = Sample()
obj.a = "Tonmay"
#Sample.a = "Tonmay" #evabe likhle change hye jabe

print(Sample.a)
print(obj.a)

#No it doesn't