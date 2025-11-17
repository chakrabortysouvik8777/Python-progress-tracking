#delete 
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    y=input("Enter the Name = ")
    x[i]=y
print(x)
p=int(input("Enter the key to be deleted = "))
f=0
for k,v in x.items():
    if k==p:
        f=1
        break
if f==1:
    del(x[k])
    print(x)
else:
    print("Deletion not Possible")