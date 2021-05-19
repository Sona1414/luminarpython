number=int(input("enter the number"))
rev=0
dup=number
while(dup>0):
    rem=dup%10
    rev=rev*10+rem
    dup=dup//10
if rev==number:
    print(number, "is palindrome")
else:
    print("not palindrome")


