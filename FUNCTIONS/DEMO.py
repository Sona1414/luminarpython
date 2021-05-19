#functions are used to perform task
#...............
#inbuilt functions
#print
#input
#range
# a=10
# print(type(a))
#
# num1=int(input())
# syntax
# def funcname(areguments):
 #statements
 # call using funcname

 #creating in 3 ways
 #func without args and without returntype
 #func with args and no returntype
 #func with args and returntype
def mult():
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    multiply=num1*num2
    print(multiply)
mult()

#functional programming
#lambda
#filter
#map
#reduce



#2nd method
def mult(num1,num2):
    res=num1*num2
    print(res)
mult(12,24)

def divide(num1,num2):
    res=num1/num2
    print(res)
divide(6,3)

#3rd method
def sum(no1,no2):
    res=no1+no2
    return res
data=sum(10.20)
print(data)