#neon 
n=int(input("enter the number="))
s=0
sq=n*n
while n>0:
    rem=sq%10
    s=s+rem
    sq=sq//10
if n==s:
    print("neon number ")
else:       
    print("not neon")