#delete an element from the list
li=[]
n=int(input("Enter the range ="))
for i in range(0,n,1):
    li.append(int(input("Enter the number =")))
print("list =",li) 
x=int(input("enter the element u want to delete="))   
for i in range(0,n,1):
    if li[i]==x:
        f=1
        break
if f==1:
    del(li[i])
    print(li) 
else:
    print("element not found")    
       