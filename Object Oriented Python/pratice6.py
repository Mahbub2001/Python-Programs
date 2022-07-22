'''
can you change the self perameter inside a class to something else (say 'turza').try chaging self to 'slf' or 'turza' and see the effects
'''
class Sample:
    a = "Turza"
    def __init__(slf,name):
        slf.name = name

obj = Sample("Turza")
print(obj.a)
        

