#remove all duplicates
li=[]
li2=[]
n=int(input("Enter the range ="))
for i in range(0,n,1):
    li.append(int(input("Enter the number =")))
print("list =",li) 
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)