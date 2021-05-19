cyear=int(input("enter the current year"))
cmon=int(input("enter the current month"))
cdate=int(input("enter the current date"))
byear=int(input("enter the birth year"))
bmonth=int(input("enter the birth month"))
bdate=int(input("enter the birth date"))
age=cyear-byear
if(cmon<bmonth):
    age-=1
    print("age is",age)
elif(cmon==bmonth):
    if(cdate<bdate):
        age-=1
        print("age is",age)
    else:
        print("age is",age)
else:
    print("age is",age)
