#list comprehension
arr=[1,2,3,4,5]
squares=[i**2 for i in arr]
print(squares)

arr1=["orange","apple","mango"]
squares=[(names,names) for names in arr1]
print(squares)

lst1=[1,2]
lst2=[10,20]
# for i in lst1:
#     for j in lst2:
#         print(i,",",j)
print1=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(print1)



lst3=[10,20,35,40]
even=[num1 for num1 in lst3 if num1%2==0]
print(even)


lst4=[7,8,9,4,3,2]
pattern=[num+1 if num>5 else num-1 for num in lst4]
print(pattern)

