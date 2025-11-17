#WAP to delete an element(key) within the dictionary
d={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the key = "))
    d[p]=input("Enter the String = ")
print(d)
x=int(input("Enter the key to be deleted = "))
f=0
for k,v in d.items():
    if k==x:
        f=1
        break
if f==1:
    del(d[k])
    print(d)
else:
    print("element not found")
    print(d)
    