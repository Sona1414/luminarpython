class Student:
    def setval(self,name,rollno,course,marks):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.marks=marks
    def print(self):
        print(self.name,self.rollno,self.course,self.marks)
f=open("student details","r")
for i in f:
    word=i.rstrip("\n").split(",")
    if int(word[3])>=190:
        name=word[0]
        rollno=word[1]
        course=word[2]
        marks=word[3]
        st=Student()
        st.setval(name,rollno,course,marks)
        st.print()