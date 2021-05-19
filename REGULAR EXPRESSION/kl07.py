#kerala vehicle
#kl07bf1234
import re
n=input("enter the string")
x="[K][L]\d{2}[A-Z]{2}\d{4}$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")