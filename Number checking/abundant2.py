#abundant number
n=int(input("enter the number="))
s=0
for i in range(1,n):
   if n%i==0:
       s=s+i 
       if s>n:
           print("abundant number")
       else:
           print("not abundant") 