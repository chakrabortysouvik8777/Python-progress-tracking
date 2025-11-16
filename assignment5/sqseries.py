#1/1^2+ 1/2^2+....+1/n^2
n=int(input("enter the range= "))
s=0
for i in range(1,n+1):
   if i==n:
       print(1,"/",i**2,end="=")
   else:
       print(1,"/",i**2,end=" + ") 
   ser=1/(i*i)
   s+=ser
print(s,end=" ")