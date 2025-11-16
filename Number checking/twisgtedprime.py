#Twisted prime number
n =int(input("enter the number = "))
f=0
g=0
s=0
d=n
for i in range(2,n):
    if n%i==0:
        f=1
        break
if f==0:
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
for i in range(2,s):
    if s%i==0:
        g=1
        break
if f==0 and g==0:
    print("twisted prime number") 
else:
    print("not twisted prime number")                 
