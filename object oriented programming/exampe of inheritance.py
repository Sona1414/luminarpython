class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Child(Person):
    def setval(self,hobbies):
        self.hobbies=hobbies
class Parent(Person):
    def set(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
    def print(self):
        print(self.name,self.age,self.gender,self.job,self.place,self.salary)
class Student(Child):
    def stdetails(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def disp(self):
        print(self.name,self.age,self.gender,self.rollno,self.school)
stud=Student()
stud.details("sona",15,"female")
stud.stdetails(101,"aloysius")
stud.disp()
par=Parent()
par.details("soman",64,"male")
par.set("seaman","abudhabi","20,000")
par.print()
