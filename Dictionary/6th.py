# valuewise search & delete the element
#keywise search
x={}
f=0
n=int(input("Enter the range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the String = ")
print(x)
value=input("Enter the String = ")
for k,v in x.items():
    if value==v:
        del(x[k])
        f=1
        break
if f==1:
    print(x)
else:
    print(f"{value} Not Found")

