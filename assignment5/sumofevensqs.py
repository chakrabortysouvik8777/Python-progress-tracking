#wap to calculate sum of squars of even numbers from 1-n using for loop
n= int(input("enter the range ="))
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i**2
print(s)