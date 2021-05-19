lst=[1,3,2,2,4,7,8,1,2]
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print(res)
