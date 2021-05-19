n=int(input("enter the number"))
sum=0
dup=n
while(dup>0):
    rem=dup%10
    sum+=rem*rem*rem
    dup=dup//10
if sum==n:
    print("yes")
else:
    print("no")