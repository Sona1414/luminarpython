class Calculator:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    def add(self):
        print("sum=",Calculator.num1+Calculator.num2)
    def subtract(self):
        print("result =",Calculator.num1-Calculator.num2)
    def multiply(self):
        print("product=",Calculator.num1*Calculator.num2)
    def divide(self):
        print("result=",Calculator.num1/Calculator.num2)
cal=Calculator()
while(True):
    ch=int(input("enter the choice"))
    if ch==1:
        cal.add()
    elif ch==2:
        cal.subtract()
    elif ch==3:
        cal.multiply()
    elif ch==4:
        cal.divide()
    else:
        print("invalid choice")
        break