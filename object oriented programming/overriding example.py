class person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print("inside person class")
        print(self.name,self.age)
class student(person):
    def details(self,school,rolno):
        self.school=school
        self.rolno=rolno
        print("inside student class")
        print(self.school,self.rolno)
st=student()
st.details("aloysius",101)