#remove---element is passed and the particular element first appeared in the list will be removed
#pop--- the list index is passed and the element present int the particular index will be deleteed
lst=[]
lst1=[]
lst2=[]
for i in range(1,101):
    lst.append(i)
print(lst)
for i in lst:
    if i%2==0:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1)
print(lst2)
