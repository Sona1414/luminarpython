#min lenght 8 and max 15
#except numbers
import re
n=input("enter the string")
x="([\D]{8,15}$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")