lst=[]
print(lst)
#to add element we can use append function, we cannot directly use the index value since there is no index
lst.append(100)
lst.append(1000)
lst.append("sona")
#lst.append(2,3,4)#error append can be used to add one element at a time
print(lst)
#extend--can be used to add multiple element at a time
lst.extend([5,7,3])
print(lst)