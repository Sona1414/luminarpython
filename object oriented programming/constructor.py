#constructor: it is used to initialise the instance variable
#constructor: is automatically invoked when the object is created



class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,self.age,self.gender)
pp=Person("sona",24,"female")
pp.print()