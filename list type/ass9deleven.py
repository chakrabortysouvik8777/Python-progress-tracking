#wap that creates a list of a numbers that are either divisible by 2 or 4 without filter
n=int(input("enter the range ="))
li=[]

for i in range(1,n+1,1):
    #li.append(i)
    #print("original list=",li)    
    if i%2==0:
        del(li[i])
    else:
        li.append(i)
print("final list=",li)         