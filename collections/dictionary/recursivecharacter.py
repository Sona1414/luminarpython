dic={}
str="abcdbca"
for i in str:
    if i not in dic:
        dic[i]=1
    else:
        print(i)
        break


