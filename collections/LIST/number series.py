#lst=[3,4,8]
#newlst=[12,11,7]
lst=[3,4,8]
newlst=[]
sum=0
for i in lst:
    sum=sum+i
for i in lst:
    j=sum-i;
    newlst.append(j)
print(newlst)