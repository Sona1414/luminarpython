def add(num1,num2): #para1,para2#FUNC DEF CONTAIN PARAMETERS
    return num1+num2

res=add(10,20)  #arg1,arg2#FUNC CALL CONTAIN ARGUMENTS
print(res)

#function name
#1.addThree()  camoline notation--first word small letter then capital letter
#2.add_three()  SNAKE NOTATION---letter then underscore
#2 is the best option to choose the function name


#if we want to add  3 elemnts we need to create another function, so to avoid thiS we
#should have the function to accept any number of arguments
def add(*args):
    res=0
    for num in args:
        res+=num
    return res

print(add(10,20,30,40))
print(add(12,24,55,60))


def print_employee(**kwargs):
    print(kwargs)

print(print_employee(id=100,nat_loc="kochi",wrk="kakkanad"))


#def print_employee(**kwargs)

#*args---can accept 0 or anynumber of arguments in the form of tuple
#**kwargs---can accept 0 or any number of arguments in the form of dictionary



