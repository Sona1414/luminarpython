import re
n=input("enter the string")
x="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
match=re.finditer(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")