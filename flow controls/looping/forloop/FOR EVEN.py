low=int(input("enter the lower limit"))
upp=int(input("enter the upper limit"))
for i in range(low,upp+1):
    if(i%2==0):
        print(i)
    i+=1