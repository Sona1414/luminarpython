import re
x="(a+[a-zA-Z0-9]*b$)"
n=input("enter the string")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")