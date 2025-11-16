#wap tp print 1+1/2+1/3+1/4.....+1/n
n=int(input("enter the range= "))
s=0    
for i in range(1,n+1):
    if i==n:
        print(1,"/",i,end="=")
    else:
        print(1,"/",i,end="+")    
    s=s+(1/i)
print(s)