#set
##how to define
# set={}
# print(type(set))
#set function can  be used to create a empty set
st=set()
print(type(st))
set={1,2,3,4}
print(type(set))
##heterogenous data
set1={2,"sona",10.4,True,False}#supports heterogenous data
print(set1)
#insertion order not preserved
set2={1,1,2,2,"sona","sona"}
print(set2)
#will not support duplicate value
st2={1,2,True}
print(st2)
st3={True,False,0,1}
print(st3)
st3={10,9,8,7,6,5,4,3,2,1}
print(st3)
#set is mutable