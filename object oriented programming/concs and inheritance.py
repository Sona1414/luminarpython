class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,rollno,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        print(self.name,self.age,self.rollno)
stu=Student(101,"SONA",15)



