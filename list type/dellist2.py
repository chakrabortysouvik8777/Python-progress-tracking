#delete an element from the list
li=[]
n=int(input("Enter the range ="))
for i in range(0,n,1):
    li.append(int(input("Enter the number =")))
print("list =",li) 
x=int(input("enter the element u want to delete="))   

i=0
while i<n:
    if li[i]==x:
        del(li[i])
        n=n-1 
        i-=1 
    i+=1    
print(li) 
