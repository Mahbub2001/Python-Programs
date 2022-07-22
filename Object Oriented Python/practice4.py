'''
add a static method in practice 3 to greet the user hello
'''

class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number**2} ")

    def cube(self):
        print(f"The value of {self.number} square is {self.number**3} ")

    def squareRoot(self):
        print(f"The value of {self.number} square is {self.number**0.5} ")

    @staticmethod
    def greet():
        print("******************Hello there welcome to the best calculator of this world***************")


a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
        

