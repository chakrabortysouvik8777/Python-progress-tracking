#harshad number
n=int(input("enter the number="))
s=0
d=n
while(n>0):
    rem=n%10
    s=s+rem
    n=n//10
    if d%s==0:
        print("harshad number")
    else:
        print("not harshad")    
    