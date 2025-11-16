#wap to print factorial of a number 
n=int(input("enter the number= "))
i=0
f=1
for i in range(1,n+1,1):
    f=f*i
print("factorial of",n,"is",f)    