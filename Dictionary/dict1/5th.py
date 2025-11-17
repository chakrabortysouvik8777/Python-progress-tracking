#WAP to delete an element(value) within the dictionary
d={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the key = "))
    d[p]=input("Enter the String = ").lower()
print(d)
x=input("Enter the String to be deleted = ").lower()
f=0
for k,v in d.items():
    if v==x:
        f=1
        break
if f==1:
    del(d[k])
    print(d)
else:
    print("element not found")
    print(d)
    