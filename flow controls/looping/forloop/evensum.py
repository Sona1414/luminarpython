low=int(input("enter the lower limit"))
upp=int(input("enter the upper limit"))
esum=0
osum=0
for i in range(low,upp+1):
    if(i%2==0):
        esum=esum+i;
    else:
        osum=osum+i;
print("even sum is",esum)
print("odd sum is",osum)