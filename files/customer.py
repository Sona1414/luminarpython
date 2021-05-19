f=open("D:\documents\customer","r")
for i in f:
    word=i.rstrip("\n").split(",")
    #print(word)
    #print(word[1],",",word[3],",",word[-1])
    #if word[-1]=="india":
        #print(word[1])
    #if int(word[3])>50:
        #print(word[1],",",word[2],",",word[3],",",word[-2],",",word[-1])
    if word[-2]=="Doctor":
        print(word[-2],",",word[1],",",word[2],word[-1],word[3])

