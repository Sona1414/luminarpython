def cube():
    num1=int(input("enter the number"))
    cube=num1*num1*num1;
    print("the cube of the number is", cube)
cube()

def cube(num1):
    cube=num1*num1*num1
    print("the cube of the number is", cube)
cube(2)


def cube(num1):
    cube=num1*num1*num1
    return cube
res=cube(4)
print("the cube of the number is", res)