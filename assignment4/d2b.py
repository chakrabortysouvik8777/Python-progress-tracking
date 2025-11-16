#wap to convert decimal to binary
n=int(input("enter the number ="))
s=""
x=n
while n>0:
    rem=n%2
    s=str(rem)+s
    n=n//2
print(x,"Binary equivalent",s)    