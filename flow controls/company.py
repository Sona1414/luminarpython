sal=int(input("enter the salary"))
exp=int(input("enter the year of service"))
bonus=sal*(5/100)
if(exp>=5):
    netbonus=bonus+sal
    print("the net bonus of the employer is", netbonus)
else:
    print("no bonus")