# def print(*args):
#     print(type(args))
#
# print(10,20,30)

def add(*args):
    res=0
    for i in args:
        res=res+i
    return res

sum=add(10,20,30)
print(sum)

def print_employee(**kwargs):
    for i,v in kwargs.items():
        print(i,"=",v)


print_employee(id=100,nat_place="thrissure",work="kakanad")

arr=[12,2,3,6,7,8]
# arr.sort()
# print(arr)
# print()
# print(arr)
#print(sorted(arr))
#difference between sort and sorted()
#sort is a method in list class that is why it is called using . operator
#while sorted is a function
