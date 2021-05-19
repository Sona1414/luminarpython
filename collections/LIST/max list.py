lst=[10,50,30,70,60,90,20]
max=lst[0]
for i in lst:
    if i>max:
        max=i
print(max)
#max function can be used
print(max(lst))
print(min(lst))
# #length of list
print(len(lst))
# #sorted
print(sorted(lst))#sorted in ascending order
lst.sort(reverse=True)
#
# print(lst)