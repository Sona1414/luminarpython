#list

lst=[]
#first method using square bracket
print(type(lst))

#2nd method usint list function
sa=list()
print(type(lst))
#supports hetrogenous data

lst=[1,10.6,"sona",True,False]
print(lst)

#whether inseryion order is preserved
lst=[10,15,6,7,3,3,2,1,1,"sona","neena"]
print(lst)

#duplicate value supported or not
lst=[10,10,10,"sona","sona"]
print(lst)

#to access each element we can use index values.. which starts from 0 to n-1
print(lst[0])
print(lst[3])

#to change an element in the list#is mutable
lst[2]=100
print(lst)
