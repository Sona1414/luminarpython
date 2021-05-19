num1=int(input("enter number 1"))
num2=int(input("enter the numebr 2"))
num3=int(input("enter number 3"))
if((num1>num2)&(num1>num3)):
    print(num1,"is highest")
elif((num2>num1)&(num2>num3)):
    print(num2,"is highest")
else:
    print(num3,"is highest")