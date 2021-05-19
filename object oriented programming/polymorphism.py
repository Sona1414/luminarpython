#exist in may forms
#overloading-- parent class and child class has the function with the same name but different number of arguments
class Student:
    def set(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print(self.name,self.rollno)
class child(Student):
    def set(self,age,gender,mark):
        self.age=age
        self.gender=gender
        self.mark=mark
        print(self.age,self.gender,self.mark)
ch=child()
ch.set(12,"female",120)
#ch.set("sona",101)--not possible causes an error