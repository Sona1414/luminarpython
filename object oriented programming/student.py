class Student:
    school="STAS"
    def setdetails(self,name,age,standard,division):#here we can use the attributes in both the functions
        self.name=name#we ca use the attributes in all the functions of the class
        self.age=age
        self.standard=standard
        self.division=division
    def printdetails(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("STANDARD",self.standard)
        print("DIVISION",self.division)
        print("SCHOOL NAME:",Student.school)
        print()
st1=Student()
st2=Student()
st1.setdetails("sona",15,10,"A")
st2.setdetails("rahul",15,10,"B")
st1.printdetails()
st2.printdetails()