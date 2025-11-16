#co-prime number
a=int(input("enter the 1st number="))
b=int(input("enter the 2nd number="))
f=0
g=0
for i in range(2,a):
    if a%i==0:
        f=1
for j in range(2,b):
    if b%j==0:
        g=1
if f==0 and g==0:
    print("co-prime")
else:    
    print("not co-prime")              
   
    