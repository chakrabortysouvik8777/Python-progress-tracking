#wap to print prime and composirte number until -1 will be encountered
f=0
cp=0
cc=0
while True:
    n=int(input("enter the number ="))
    if n==-1:
        break
    else:
        i=1
        while i<=n:
            if n%i==0:
                f=f+1
            i=i+1
        if f==2:
            print("prime number")        
            cp=cp+1
        else:
            print("composite number")
            cc=cc+1
        f=0
print("number of prime =",cp)        
print("number of composite =",cc)                
    