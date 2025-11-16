#tech number
n=int(input("enter the number = "))
c=0
d=n
while(n>0):
    c+=1
    n=n//10
    k=c//2
if c%2==0:
    p=d%10**k
    q=d//10**k
    s=p+q
    if  d==s**2:
         print("tech number") 
    else:
         print("not tech")         
#else:
 #   print("not tech")         