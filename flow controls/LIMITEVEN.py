limit=int(input("enter the limit"))
for i in range(2,limit+1):
    flag=0;
    for j in(2,i):
        if(i%j==0):
            flag=1
    if(flag==1):
        print(i)








