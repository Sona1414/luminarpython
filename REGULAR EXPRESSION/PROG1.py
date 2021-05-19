import re
n="hello"
x="\w*"#we have to specify both rules and quantifier
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")


import re
n="57kg"
x="\d{2}[a-z]{2}"#we have to specify both rules and quantifier
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

import re
n=int(input("Enter the 10 digit number"))
x="[0-9]{10}"
match=re.fullmatch(x,str(n))
if match is not None:
    print("valid")
else:
    print("invalid")

import re
n=input("enter the number")
x="\W['0-9']{12}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid indian number")
else:
    print("invalid")


