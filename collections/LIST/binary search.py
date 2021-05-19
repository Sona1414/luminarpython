#lst=[2,1,4,5,3]
#
# 1.sort the given list
#   lst=[1,2,3,4,5]
# 2.
lst=[1,6,4,3,2,5]
lst.sort()
print(lst)
element=int(input("enter the element"))
len=len(lst)
low=0
upp=len-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if element>lst[mid]:
        low=mid+1
    elif element<lst[mid]:
        upp=mid-1
    else:
        flag=1
        break
if(flag==1):
    print("found")
else:
    print("not found")


