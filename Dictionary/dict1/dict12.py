# keywise element search 
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the String = ")
print(x)
p=int(input("Enter the Key to be searched for = "))
f=0
for k,v in x.items():
    if k==p:
        f=1
        break
if f==1:
    print("Found")
else:
    print("NOT Found")