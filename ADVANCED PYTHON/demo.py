a=2
B=4
def printa():
    global a
    B=2
    print(B)
    print(a)
    a=a+2
    B=B+2
printa()
print(a)
print(B)
