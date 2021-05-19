class Employee:
    def __init__(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
    def print(self):
        print(self.name,self.id,self.desig,self.salary)
emp1=Employee("sona",101,"developer",1500)
emp1.print()