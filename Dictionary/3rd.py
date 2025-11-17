#WAP to take input into a dictionary run time & print the dictionary
x={}
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    x[int(input("Enter the key = "))]=int(input("Enter the Value = "))
print(x)

for k,v in x.items():
    print(k,":",v)

for v in x.values():
    print(v**2,end=' ')
    
