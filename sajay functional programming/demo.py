#LAMBDA FUNCTION---ANONYMOUS FUNCTION WHICH MEANS IT DOESNT HAVE A NAME
#SO REMOVE ALL THE NAMES IN THE BASIC FUNCTION
def add(num1,num2):
    print(num1+num2)
add(10,20)

#using lambda function
f=lambda num1,num2:num1+num2
print(f(10,209))

#MAP FUNCTION

# def square(num):
#     return num**2

arr=[1,2,3,4,5]
squarelist=list(map(lambda num:num**2,arr))
print(squarelist)

# def to_upper(name):
#     return name.upper()

lst=["sona","rahul"]
lst1=list(map(lambda name:name.upper(),lst))
print(lst1)


lst=[7,8,9,3,2,1]
newlst=[]
for i in lst:
    newlst.append(i+1) if i>5 else newlst.append(i-1)# if i>5:
    #     newlst.append(i+1)
    # else:
    #     newlst.append(i-1)
print(newlst)

lst2=["sona","rahul"]
astart=list(filter(lambda name:name[0]=="s",lst2))
print(astart)
