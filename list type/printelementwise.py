#wap to print any input element wise
li=[]
n=int(input("enter the range ="))
for i in range(0,n,1):
    x=int(input("enter the number ="))
    li.append(x)
print("List =",li)    
for i in li:
    print(i,end="")
#li=li.sort(reverse=True)
#print( "list =", li)