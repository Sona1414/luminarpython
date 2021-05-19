f=open("D:\documents\customer","r")
dic={}
for i in f:
    word=i.rstrip("\n").split(",")
    #print(word)
    fname=word[4]
    if fname not in dic:
        dic[fname]=1
    else:
        dic[fname]+=1
for k,v in dic.items():
    print(k,",",v)