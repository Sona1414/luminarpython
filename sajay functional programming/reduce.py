#map anf filter functions are defined in built ins.py file so we do not require to import any packages
#the lambda func in map and filter can contain only one argument
#reduce func can be used only if there is a single output,the labda func in reduce function has 2 arguments
#reduce is defined in functools file ,so it has to be imported
import functools
arr=[1,2,3,4,5]
total=functools.reduce(lambda num1,num2:num1+num2,arr)
print(total)

from functools import *
arr=[1,2,3]
tot=reduce(lambda num1,num2:num1+num2,arr)
print(tot)

#print the highest
arr=[1,5,67,89,90]
highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
print(highest)

#reduce can have only number arguments beacuse it is used to find the total,highestor minimum value