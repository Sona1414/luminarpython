f=open("D:\documents\Temperature","r")
dic={}
for i in f:
    words=i.rstrip("\n").split(" ")
    #print(words)
    year=words[0]
    temp=int(words[-1])
    if year not in dic:
        dic[year]=temp
        max=temp
    else:
        if temp>max:
            dic[year]=temp
for k,v in dic.items():
    print(k,",",v)




