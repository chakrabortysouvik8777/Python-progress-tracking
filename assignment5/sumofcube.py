#wap to calculate sum of cubes of numbers from 1-n using for loop
n= int(input("enter the range ="))
s=0
for i in range(1,n+1):
    s=s+i*i*i
print(s)