#SINGLE INHERITANCE
class Person:
    designation="student"
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    # def print(self):
    #     print("name:",self.name)
    #     print("age:",self.age)
    #     print("gender:",self.gender)
class Student(Person):
    def setval(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def disp(self):
        print("name:", self.name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("designation:",Person.designation)
        print("Roll no:",self.rollno)
        print("School:",self.school)
stu1=Student()
stu1.details("rahul",15,"male")
stu1.setval(101,"aloysius")
#stu1.print()
stu1.disp()