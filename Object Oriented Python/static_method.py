class Employee:
    company = "Google"
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
        
    @staticmethod#eti dile self use kora jabe na#na dile self use krte hbe
    def greet():
        print("Good Morning,Sir")
    @staticmethod
    def time():
        print("The time is 9 am in the morning")

turza = Employee()
turza.salary = 10000
turza.getSalary("Thanks!")
turza.greet() 
turza.time()
