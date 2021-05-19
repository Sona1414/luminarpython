#dictionary

dic={}
print(type(dic))
#how to store values in dictionary
#key value pairs
#syntax for entering data
#keys:values

#name:luminar,loc:kakkanad,course:python

#keys:name,loc,course

#values:luminar,kakkanad,python

dic={"name":"luminar","loc":"kakkanad","course":"python","marks":240,"data":10.25}
print(dic)

#it supports heterogenous data

#insertion order is preserved

dic1={"name":"sona","age":25,"age":25}
print(dic1)

#it supports duplicate values
#it does not supports duplicate keys

# how to collect a value from dictionary
# using the key
print(dic["name"])#we can get the single value by specifying the name of dictionary followed by the key name inside the double quotes
print(dic["loc"])
#OUTPUT
#name:luminar
#loc:kakkanad
for i in dic:
    print(i,":",dic[i])
#dictionary is mutable, ie the value can be updated
dic["marks"]=250
dic["data"]=15.5
dic["marks"]+=10
print(dic)
#how to delete a value
del dic["name"]
print(dic)
dic.pop("course")
print(dic)



