#wap to delete an items using empty list
li=[]
n=int(input("enter the range ="))
for i in range(0,n,1):
    li.append(input("enter the number ="))
print("list =",li) 
for i in range(0,n,1):
    if li[i]==" ":
        f=1
        break  
if f==1:
    del(li[i])
    print(li) 
else:
    print("element not found")      