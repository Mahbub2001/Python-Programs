#class attributes : 

class Employee:
    company = "Google"

turza = Employee()
tonmay = Employee()
print(turza.company)
print(tonmay.company)

##class company change
Employee.company = "Youtube"
print(turza.company)
print(tonmay.company)

#Instance Atribute

class Employee:
    company = "Google"
    salary = 100

turza = Employee()
tonmay  = Employee()

turza.salary = 300#instance attribute
# tonmay.salary = 400#instance atribute

print(turza.salary)
print(tonmay.salary)