#wap to convert binary to decimal
n=input("enter the number =")
print(n)
x=int(n)
s=0
i=1
while x>0:
    rem=x%10
    p=rem*i
    s=s+p
    x=x//10
    i=i*2
print(n,"decimal is",s)