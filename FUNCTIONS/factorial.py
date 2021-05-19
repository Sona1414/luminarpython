# def fact():
#     num1=int(input("enter the number"))
#     res=1
#     for i in range(1,num1+1):
#         res*=i
#     print(res)
# fact()
#
# #2nd method
# def fact(num1):
#     res=1
#     for i in range(1,num1+1):
#         res*=i
#     print(res)
# fact(5)
#3 method
def fact(num1):
    res=1
    for i in range(1,num1+1):
        res=res*i
    return res
data=fact(5)
print(data)