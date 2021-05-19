lst=[[101,"sona",21,2500],[102,"ammu",21,2000]]
#nested list-- multiple list inside a list
#101 sona 21
#102 ammu 21
for i in lst:
     print(i)
#sona
#ammu
for i in lst:
    print(i[1])

#salary above 2500
for i in lst:
    if i[3]>=2500:
        print(i[1])

#sum of salaray
sum=0
for i in lst:
    sum=sum+i[3]
print(sum)
