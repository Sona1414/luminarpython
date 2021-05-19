#functional programming

#to reduce the program length

#lambda
#map
#filter
#list comprehension


#lambda function--an anonymous function--ie nameless or unknown
def sum(num1,num2):
    s=num1+num2
    return s
print(sum(10,20))

#convert the function into lambda

f=lambda num1,num2:num1+num2
print(f(10,20))
f=lambda num1,num2:num1-num2
print(f(10,-20))
f=lambda num1,num2:num1*num2
print(f(10,10))
f=lambda num1,num2:num1/num2
print(f(10,2))

#map

#lst=[10,20,30,40]-->f(x)..ie f(x) is a function applied on all the objects in the
# list and the function is to find the square
#[100,400,900,1600]

#map is used when all the objects in the list has a corresponding output
#[ae,ab,ac,eb,ed]-->f(x)--ie f(x) convert to upper case
#[AE,AB,AC,EB,ED]


#filter

#[1,2,3,4,56,7,8,9,10]-->WE WANT ONLY THE EVEN NUMBERS FROM THE LIST
#here we can use filter
#[2,4,6,8,10]

#syntax
#............................................

#map(function,iterable)

lst=[1,2,3,4,5,6,7,8,9]
# def square(num):
#     return num*num
#this func can be replaced  using lamba
#s=list(map(square,lst))
#print(s)

s=list(map(lambda num:num*num,lst))
print(s)



#filter(function,iterable)

lst1=[1,2,3,4,5,6,7,8,9,10]
# def even(num):
#     if num%2==0:
#         return num
# ev=list(filter(even,lst1))
# print(ev)

ev=list(filter(lambda num:num%2==0,lst1))
print(ev)



#list comprehension
lst=[]
for i in range(1,51):
    lst.append(i)
print(lst)

#reduce the above code using list comprehension
lst2=[i for i in range(1,51)]
print(lst2)
#in syntax: first specify the value to be printed then specify the range
#to append the even numbers to the list
lst3=[i for i in range(1,51) if(i%2==0)]
print(lst3)
#print,range,condition
lst4=[i*i if i%2==0 else i*i*i for i in range(1,10)]
print(lst4)
lst5=["even" if i%2==0 else "odd" for i in range(1,10)]
print(lst5)



