mark1=int(input("enter the mark 1"))
mark2=int(input("enter the mark 2"))
mark3=int(input("enter the mark 3"))
mark4=int(input("enter mark 4"))
total=mark1+mark2+mark3+mark4
if(total>=180)&(total<=200):
    print("A+")
elif(total>=160)&(total<=179):
    print("A")
elif(total>=140)&(total<=159):
    print("B+")
elif(total>=120)&(total<=139):
    print("B")
elif(total>=100)&(total<=119):
    print("C+")
elif(total>=80)&(total<=99):
    print("C")
elif(total>=60)&(total<=79):
    print("D+")
else:
    print("fail")

#simpler method
#total>=180
#160<=total<=179
#
