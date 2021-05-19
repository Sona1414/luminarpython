lst=[25,67,22,33,90]
for i in range(0,len(lst)-1):
    for j in range(0,len(lst)-i-1):
     if lst[j]>lst[j+1]:
        temp=lst[j]
        lst[j]=lst[j+1];
        lst[j+1]=temp
print(lst)