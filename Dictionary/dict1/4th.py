#WAP to take input (runtime input key & value) within the dictionary & print it & clear it
d={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=int(input("Enter the key = "))
    d[p]=input("Enter the String = ")
print(d)
for k,v in d.items():
    print(k,":",v)
d.clear()
print(d)    