class person:
    def setvalues(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Name:",name)
        print("Age:",age)
        print("Gender:",gender)
class student(person):
    def setstu(self,rollno,schoolname):
        self.rollno=rollno
        self.schoolname=schoolname
        print("Roll no:",self.rollno)
        print("Schoolname:",self.schoolname)
class teachers(person):
    def settea(self,subjects):
        self.subjects=subjects
        print("subjects")
class extra(student):
    def setextra(self,activity1,activity2):
        self.activity1=activity1
        self.activity2=activity2
        print("ACTIVITY 1:",activity1)
        print("ACTIVITY 2:",activity2)
ex=extra()
ex.setvalues("sona",15,"female")
ex.setstu(101,"aloysius")
ex.setextra("dancing","running")
te=teachers()
te.setvalues("amritha",25,"female")
te.settea("computer")