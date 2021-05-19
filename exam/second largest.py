lst=[1,4,3,5,6,7,8,22,23]
max=lst[0]
for i in lst:
    if i>max:
        max=i
lst.remove(i)
max=lst[0]
for i in lst:
    if i>max:
        max=i
print(max)
