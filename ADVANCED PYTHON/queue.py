size=int(input("enter the size of the queue"))
front=-1
rear=-1
lst=[]
def insert():
    global front, rear
    if rear==size-1:
        print("stack is full")
    elif front==rear==-1:
        element=int(input("enter the element"))
        lst.append(element)
        front=0
        rear=0
        print(lst)
    else:
        element=int(input("enter the element"))
        lst.append(element)
        rear=rear+1
        print(lst)
def delete():
    global front,rear
    if front==-1:
        print("queue is empty")
    elif front==rear:
       print("deleted item is",lst[front])
       lst.pop(front)
       front=rear=-1
       print(lst)
    else:
        print("deleted item is",lst[front])
        lst.pop(front)
        front=front+1
        print(lst)
while(True):
    ch=int(input("enter the choice"))
    if(ch==1):
        insert()
    elif(ch==2):
        delete()
    else:
        print("invalid choice")
        break



