#WAP to take input into a dictionary run time & print the dictionary
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    x[i]=input("Enter the String = ")
print(x)

for k,v in x.items():
    print(k,":",v)
