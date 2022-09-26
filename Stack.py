#Stack
stk=[]
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push():
    item=int(input('Enter a number: '))
    stk.append(item)
    top=len(stk)-1
def Pop():
    if isEmpty(stk):
        return 'Underflow'
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Peek():
    if isEmpty(stk):
        return 'Underflow'
    else:
        top=len(stk)-1
        print(stk[top])
def Display():
    if isEmpty(stk):
        print('Stack is Empty')
    else:
        top=len(stk)-1
        print(stk[top])
        for i in range(top-1,-1,-1):
            print(stk[i])
top=None
def Main():
    while True:
        print('Stack Operations')
        print('1.Push\n2.Pop\n3.Peek\n4.Display')
        ch=int(input('Enter your choice: '))
        if ch==1:
            Push()
        elif ch==2:
            Pop()
        elif ch==3:
            Peek()
        elif ch==4:
            Display()
        else:
            break
Main()        
        
