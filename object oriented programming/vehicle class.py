class Vehicle:
    def features(self,name,tyres):
        self.name=name
        self.tyres=tyres
        print(self.name,self.tyres)
ab=Vehicle()
ac=Vehicle()
ae=Vehicle()
ab.print("car",4)
ac.print("bike",2)
ae.print("auto",3)