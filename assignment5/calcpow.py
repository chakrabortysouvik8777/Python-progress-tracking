#wap to calculate pow(x,n)using for loop
import math
n=int(input("enter the number= "))
x=int(input("enter the base= "))

for x in range(x,0,-1):
 r=pow(x,n)
print(r)    