#keywise search
x={}
n=int(input("Enter the range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the String = ")
print(x)
key=int(input("Enter the Key = "))
print(x.get(key,0))