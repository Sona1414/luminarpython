#regular expression are used for pattern matching ie while filling a form in the field of mob no we have to
#specify the number itself we cannot use string, so in this purpose we use pattern matching
#ie for validation
#the package re is used for regular expression in python
import re
count=0
matcher=re.finditer("ab","ababab")#finditer is used for iteration we have to specify the pattern to be find
#and the string which has  to be searched
#print(matcher)#it only returns the memory location
for i in matcher:
    print("match available at:",i.start())#return the position where the match has found
    print("group=",i.group())
    print()
    count+=1
print("count=",count)