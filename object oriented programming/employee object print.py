class Employee:
    def __init__(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
        print(self.name,self.id,self.desig,self.salary)
    def __str__(self):
        return self.name+str(self.id)
emp=Employee("sona",101,"manager",1200)
print(emp)
