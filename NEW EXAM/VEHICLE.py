class Vehicle:
    def setvalues(self,name,tyres):
        self.name=name
        self.tyres=tyres
        print("name:",self.name)
        print("tyres:",self.tyres)
class Bus(Vehicle):
    def set(self,cmpname):
        self.cmpname=cmpname
        print("company name:",self.cmpname)
b1=Bus()
b1.setvalues("BUS1",4)
b1.set("abc")