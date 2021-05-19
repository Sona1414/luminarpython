f=open("myfile","r")

f1=open("copyfile","w")
for data in f:
    f1.write(data)
print(f1)