#tuples

#how to define

tp=()
print(type(tp))
#we can also use tuple function
#tp=tuple()

#supports heterogenous
tp=(1,10.5,"sona",True,False)
print(tp)

tp2=(1,2,3,10,5,7,10,5,5,5)
print(tp2)#insertion order preserved#duplicates are allowed

tp(2)=10
print(tp)
#immutable cannot be updated


