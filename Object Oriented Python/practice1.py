'''
creat a class programmer for storing information of few programmers working at microsoft
'''

class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product where he work {self.product}")

turza = Programmer("Turza","Skype")
tonmay = Programmer("Tonmay","Github")
turza.getInfo()
tonmay.getInfo()
       
