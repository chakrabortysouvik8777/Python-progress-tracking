#spy number
n=int(input("enter the number="))
s=0
m=1
d=n
while (n>0):
    rem=n%10
    s=s+rem
    m=m*rem
    n=n//10
if s==m:
    print("spy no")
else:
    print("not spy")    