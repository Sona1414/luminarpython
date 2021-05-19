lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
while(lower<=upper):
    if(lower%2==0):
        print(lower, "is even")
    lower+=1