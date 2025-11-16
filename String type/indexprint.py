#wap print 1st index element of a string 
n=int(input("enter the range ="))
li=[]
for i in range(0,n,1):
    li.append(input("enter the string ="))
    print("list =",li)
for i in li:
    print(li[0],end=" ")    
    