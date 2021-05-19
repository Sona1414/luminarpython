class students:
    def setvalues(self,name,course,rollno,mark):
        self.name=name
        self.course=course
        self.rollno=rollno
        self.mark=mark
        print("name:",self.name)
        print("course:",self.course)
        print("roll no:",self.rollno)
        print("marks:",self.mark)
st1=students()
f=open("student","r")
lst=[]
for i in f:
    word=i.rstrip("\n").split(",")
    lst.append(word)
for i in lst:
    if i[3]>max:





