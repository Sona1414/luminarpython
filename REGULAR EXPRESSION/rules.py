import re
x="[abc]"#this rule means either a or b or c is present
match=re.finditer(x,"ab dct$")
for i in match:
    print(i.start())
    print(i.group())


import re
x="[^abc]"#this rule means either a or b or c is present
match=re.finditer(x,"ab dct$")
for i in match:
    print(i.start())
    print(i.group())

import re
x="[a-z]"#this rule means either a or b or c is present
match=re.finditer(x,"ab dct$")
for i in match:
    print(i.start())
    print(i.group())

import re
x="[A-Z]"
match=re.finditer(x,"ab dctA$")
for i in match:
    print(i.start())
    print(i.group())

import re
x="[a-zA-Z]"
match=re.finditer(x,"ab dcAt$")
for i in match:
    print(i.start())
    print(i.group())


import re
x="[0-9]"
match=re.finditer(x,"ab dc105t$")
for i in match:
    print(i.start())
    print(i.group())


import re
x="[^a-zA-Z0-9]"
match=re.finditer(x,"ab dc105t$")
for i in match:
    print(i.start())
    print(i.group())


import re
x="\s"
match=re.finditer(x,"ab dc105t$")
for i in match:
    print(i.start())
    print(i.group())

import re
x="\d"
match=re.finditer(x,"ab dc1t$")
for i in match:
    print(i.start())
    print(i.group())

import re
x="\D"
match=re.finditer(x,"ab dc105t$")
for i in match:
    print(i.start())
    print(i.group())

import re
x="\w"
match=re.finditer(x,"abc dc105t$")
for i in match:
    print(i.start())
    print(i.group())


#basic rules in regular expression
#x=['abc'] either a or b or c
#x=['^abc']except abc
#x=['a-z'] a to z
#x=['A-Z'] A to Z
#X=['a-zA-Z'] BOTH A TO Z AND a to z--to include more than one rule just add ith without using space or comma
#x=[0-9] 0 to 9
#x=['^a-zA-Z0-9'] for special characters
#x='\s'checks space
#x='\d' checks the digit
#x='\D' EXCEPT DIGIT
#x='\w' all words except special characters
#x='\W' for special characters
