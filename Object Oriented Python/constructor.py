class Employee:
    company = "Google"

    def __init__(self,name,salary,subunit):#ekhane self na dileo hoy ..automatic pass hoye jay
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employe is created")

    def getDetails(self):
        print(f"The name of the eployee is {self.name}")
        print(f"The name of the eployee is {self.salary}")
        print(f"The name of the eployee is {self.subunit}")
        
    def getSalary(self,signature):
        print(f"Salaray for this employee working in {self.company} is {self.salary}\n{signature}")
        
    @staticmethod#eti dile self use kora jabe na#na dile self use krte hbe
    def greet():
        print("Good Morning,Sir")
   
    @staticmethod
    def time():
        print("The time is 9 am in the morning")

turza = Employee("Turza",100,"YouTube")
# turza = Employee() #evabe likhle error dekhabe
turza.getDetails()