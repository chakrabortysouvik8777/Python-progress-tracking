# armstong number
n=int(input("enter the number="))
s=0
d=n
c=0
while n>0:
    c+=1
    n=n//10
n=d
while(n>0):
    rem=n %10
    s+=rem ** c
    n=n//10
if s==d:
    print("armstrong number ")  
else:
    print("not armstrong")   
          