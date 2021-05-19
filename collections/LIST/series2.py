lst=[10,20,21,22,25,26,27,28]
index=0
for i in lst:
    index+=1
    print(i**index)

#ANOTHER METHOD
cnt=0
for i in range(0,len(lst)):
    cnt+=1
    print(lst[i]**cnt)



