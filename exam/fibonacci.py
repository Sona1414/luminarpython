a=0
b=1
i=1
limit=int(input("enter the limit"))
print(a)
print(b)
while(i<=limit):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
