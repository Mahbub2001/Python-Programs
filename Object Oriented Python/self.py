class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")


turza = Employee()
turza.salary = 1000
turza.getSalary() # here self is harry # Employee.getSalary(turza) #evabeo hbe
