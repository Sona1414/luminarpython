#unexpected errors are called exception
#code is correct but the error can occur while reading a value
#
a=int(input("enter the number 1"))
b=int(input("enter the number 2"))
#
try:
     print(b)
     print(a/b)

except:
     print("exception occured")

#list index out of range--- exception
a=[1,2,3]
i=int(input("enter the index"))
try:
    print(a[i])
except:
    print("exception occured")
finally:
    print("inside finally")

#finally block
#finally works in both case even in exception or not.
#try is executed everytime
#except is executed only if the try block has error
#finally is executed all the time

