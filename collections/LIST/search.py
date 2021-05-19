lst=[12,13,14,15,16,17]
element=int(input("enter the element to be searched"))
flag=0
for i in lst:
    if(i==element):
        flag=1
        break
if flag==1:
    print("found")
else:
    print("not found")