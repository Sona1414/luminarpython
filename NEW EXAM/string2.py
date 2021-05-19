import re
x="[A-Z]{1}[a-z]+"
n=input("enter the string")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")