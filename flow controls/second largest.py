num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if(num1>num2)& (num1>num3):
    higest=num1;
    if(num2>num3):
        print("second largest is", num2)
    else:
        print("second largest is", num3)
elif(num2>num1)&(num2>num3):
    highest=num2;
    if (num1 > num3):
        print("second largest is", num1)
    else:
        print("second largest is", num3)
else:
    highest=num3;
    if (num1 > num2):
        print("second largest is", num1)
    else:
        print("second largest is", num2)


#current year current month current day
#birth year birth month birth date
#print age

