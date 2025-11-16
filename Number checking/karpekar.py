#karpekar number
n=int(input("enter the number="))
sq=n*n
d=sq
c=0
a=n
while(n>0):
    c+=1
    n=n//10
p=d%(10**c)    
s=d%(10**c)  
if p+s==a:
    print("karpekar number") 
else:
    print("not karpekar")    
       