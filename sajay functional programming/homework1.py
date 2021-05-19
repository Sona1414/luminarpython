lst=[7,8,9,4,3,1]
lst1=[]
for i in lst:
    if i>5:
        i=i+1
    else:
        i=i-1
    lst1.append(i)
print(lst1)