#wap to store the positive and negative element within 2 diff list
li=[]
posli=[]
negli=[]
n=int(input("enter the range ="))
for i in range(0,n,1):
    li.append(int(input("enter the number =")))
print("list =",li) 
for i in li:
    if i>0:
        posli.append(i)
    elif i<0:
        negli.append(i)
print("positive list =",posli)
print("negative list =",negli)                 
