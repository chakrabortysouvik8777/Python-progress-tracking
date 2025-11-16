 #stack
stack=[]
def push(stack):
    name=input("enter the element =")
    stack.append(name)
    print("updated stack=",stack)
def pop(stack):
    if len(stack):
        print("element deleted",stack.pop())
        print("updated stack",stack)
    else:
        print("stack is empty")
while True:
    print("1.push")
    print("2.pop")
    print ("3.display")
    choice=input("enter the choice =")
    if choice=="1":
        push(stack)  
    elif choice=="2":
        pop(stack)
    elif choice=="3":
        break
    else:
        print("invalid")                      