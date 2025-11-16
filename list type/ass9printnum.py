#wap that creates a list of a numbers that are either divisible by 2 or 4 without filter
n=int(input("enter the range ="))
li=[]
for i in range(1,n+1,1):
    if i%2==0 or i%4==0:
        li.append(i)
print(li)    