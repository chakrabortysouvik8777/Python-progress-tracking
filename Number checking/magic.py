#magic number 
n=int(input("enter the number="))
s=0
while(n>0):
    rem=n%10
    s=s+rem
    n=n//10
if s==0 or s==1:
    print("magic number ")
else:
    print("not magic")