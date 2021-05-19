class Student:
    def setval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
stu1=Student()
f=open("students","r")
for i in f:
    word=i.rstrip("\n").split(",")
    name=word[0]
    age=word[1]
    stu1.setval(name,age)



