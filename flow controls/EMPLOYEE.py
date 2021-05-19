age=int(input("enter the age"))
sex=input("enter sex(m or f)")
marital=input("enter marital status(y or n)")
if(sex=="f"):
    print("urban areas")
elif(20<=age<=40):
    print("work in anywhere")
elif(40<=age<=60):
    print("urbAN ONLY")
else:
    print("error")
