f=open("newscutting","r")
dic={}
for i in f:
    words=i.split(" ")
    print(words)
for i in words:
    if i  not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for k,v in dic.items():
    print(k,",",v)

