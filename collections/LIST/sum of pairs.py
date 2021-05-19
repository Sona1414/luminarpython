lst=[1,2,3,4,5,6]
element=int(input("enter the element"))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==element):
            print(lst[i],",",lst[j])