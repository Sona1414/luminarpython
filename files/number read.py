f=open("numbers","r")
lst=[]
sum=0
for i in f:
    lst.append(int(i))
print(lst)
print(sum(lst))
#to remove the end character

#rstrip

#lst.append(i.rstrip("\n")

data="hello\n"
data1=data.rstrip("/n")
print(data1)

#to remove the first element

data="hello\n"
data1=data.lstrip("h")
print(data1)
