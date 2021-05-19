#quantifiers are used to extend or elaborate the rules
#1. x="a+" #a including group
import re
x="a+"
r="aaa abc acc ad"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#2.x="a*" count including zero number of a#here out will be the position athe if a group contains all "a"
#only one position is returned and the others are skipped
import re
x="a*"
r="aaa abc acc ad"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#3.x="a?"each position is returned
import re
x="a?"
r="aaa abc acc ad"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#4.x="a{2}" if the group contains 2 a's together the position is returned
import re
x="a{2}"
r="aaa abc aacc ada"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#5.x="a{2,3}" minimum 2 and maximum 3 nos of a appeared together can considered
import re
x="a{1,3}"
r="aaa abc aaacc adaaaa"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#6.x="^a" checks whether the entire string starts with "a' not each word
import re
x="^a"
r="aaa abc aacc ada"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#7.x="a$"checks whether th string ends with a
import re
x="a$"
r="aaa abc aacc ada"
match=re.finditer(x,r)
for i in match:
    print(i.start())
    print(i.group())
print()
#list of quantifiers
#x="a+" a including group
#x="a*" considers all th postions but returns a also if there is a otherwise only position
#x="a?" returns each position containing a rather than skipping groups
#x="a{2}' returns the postion where 2 a's are occured together
#x={2,3} returs the position containing minimum 2 a's and maximum 3a's
#x="^a'checks whether thw string starts with a
#x="a$'checks whether the string end with string