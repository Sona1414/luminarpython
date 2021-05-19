#object oriented programming
#create all the programs as objects using a class for reusability
#multiple objects from a single class can be derived
#class: design pattern --tv#plan
#object:real world entity--sony samsung#different houses
#references: name that refers a memory location of a object--remote#house name
class Person:#class name should always start with capital letter
    def print(self,name,age,gender):#self is a instance variable which defines the print function is inside the person class
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print function",self.name,self.age,self.gender)
pe=Person()#creating objects references
re=Person()
pe.print("sona",24,"female")
re.print("rahul",24,"male")
#attribute are given inside the function brackets
#function name should always start with small letter