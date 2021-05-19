#COMBINATION OF upper case and lower case but ending with a number
import re
x="([a-zA-Z]+\d{1}$)"
n=input("enter the string")
match=re.fullmatch(x,str(n))
if match is not None:
    print("valid")
else:
    print("invalid")