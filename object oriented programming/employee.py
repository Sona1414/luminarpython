class Employee:
    cmpname="Maersk"#static variable
    def setval(self,name,id,desig,salary):
        self.name=name#instance variable because it is declared inside a function
        self.id=id
        self.desig=desig
        self.salary=salary
    def print(self):
        print("NAME:",self.name)
        print("ID:",self.id)
        print("DESIGNATION:",self.desig)
        print("SALARY:",self.salary)
        print("COMPANY NAME:",Employee.cmpname)
emp1=Employee()
emp1.setval("Rahul",1414,"3rd Officer","1,00,000")
emp1.print()



#in oob 2 types of variable are present
#1.static variable is related to class ie it is declared inside the class
#called using class name
#2.instance variable related to methods
#called using self keyword