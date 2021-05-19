def div(num1,num2):
    try:
        return num1/num2#the statement where the error occurs has to be in try block
    except Exception as e:#Exception is the class which contains all the exception "as"
        print(e.args)# is used for alias e is the other name
#e.args is used to get the actual exception in the console
res=div(5,0)