classheld=int(input("enter the number of class held"))
classattend=int(input("number of class attended by student"))
#cutoff= (classheld)*(75/100)
percent=(classattend/classheld)*100
if(percent<75):
    print("cannot attend")
else:
    print("can attend")