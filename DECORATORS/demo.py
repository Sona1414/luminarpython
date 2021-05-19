def div(num1,num2):
    return(num1/num2)
def sub(num1,num2):
    return(num1-num2)

res=div(2,10)
print(res)
sub1=sub(2,10)
print(sub1)

#here we want to take the highest number as the first value always in both the function
#which means we have to add some code to the functions
def div(num1,num2):
    if num1<num2:
        (num1,num2)=(num2,num1)
    return num1/num2
def sub(num1,num2):
    if num1<num2:
        (num1,num2)=(num2,num1)
    return num1-num2

res=div(2,10)
print(res)
sub1=sub(2,10)
print(sub1)
#in both the functions we have added the same code,so if want want to add a feature to the function
#a common feature without changing the definition of the function we  can use decorators

def dec_number(func):#this is the decorator function:decorator func always take the function on which
                    #features has to be added as arguments
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return wrapper
#decorator always has a inner func,it can have any name,here it named as wrapper,it has the same number
#of arguments of the func to which the decorators has to be added


@dec_number
def div(num1,num2):
    return num1/num2


@dec_number
def sub(num1,num2):
    return num1-num2

result1=div(5,10)
print(result1)
result2=sub(2,5)
print(result2)