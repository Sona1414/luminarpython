lst=[10,20,21,22,23]
lst1=[20,21,10,22,23]
flag=0
for i in lst:
    for j in lst1:
        if i==j:
            flag=1
            continue
        else:
            flag=0
if flag==1:
    print('same')
else:
    print("not same")
