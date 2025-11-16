#dissarium number
n=int(input("enter the number="))
s=0
d=n
c=0
while(n>0):
    n=n//10
    c+=1
n=d
while(n>0):
    rem=n%10
    s=s+rem**c
    c-=1
    n=n//10
if s==d:
        print("dissarium number")
else:
        print("not dissarium")
                  