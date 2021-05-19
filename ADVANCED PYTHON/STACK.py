top=-1
lst=[]
size=int(input("enter the size of the stack"))
def push():
    global top
    if top==size-1:
        print("stack is full")
    else:
        element=int(input("enter the element"))
        lst.append(element)
        top=top+1
        print(lst)
def pop():
    global top
    if top==-1:
        print("stack is empty")
    else:
        print("the deleted item is",lst[top])
        lst.pop(top)
        top=top-1
        print(lst)

while(True):
    ch = int(input("enter the choice:(1/2)"))
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    else:
        print("invalid choice")
        break






