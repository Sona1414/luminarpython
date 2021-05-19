str=input("enter the string")
len=len(str)
flag=0
for i in range(0,(len//2)+1):
    for j in range(len-1,(len//2),-1):
        if str[i]==str[j]:
            flag=1
            continue
if(flag==1):
    print("yes")
else:
    print("no")