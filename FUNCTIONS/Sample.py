import FUNCTIONS.ARITHEMETIC

# addition=FUNCTIONS.ARITHEMETIC.add(10,20)
# print(addition)


# syntax
# import packagename.module
#
#  packagname.module.functionname(argumnt list)
#
# subs=FUNCTIONS.ARITHEMETIC.sub(50,30)
# print(subs)
# mult=FUNCTIONS.ARITHEMETIC.multiply(10,5)
# print(mult)
# div=FUNCTIONS.ARITHEMETIC.divide(50,5)
# print(div)

#to remove the drawback
#............................

from FUNCTIONS.ARITHEMETIC import *
add1=add(10,20)
print(add1)

sub1=sub(10,5)
print(sub1)