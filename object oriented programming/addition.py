class Addition:
    def setval(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def print(self):
        print("the sum is", self.num1+self.num2)
ab=Addition()
ae=Addition()
ab.setval(10,20)
num1=int(input("enter the number1"))
num2=int(input("enter the number 2"))
ab.print()
ae.setval(num1,num2)
ae.print()