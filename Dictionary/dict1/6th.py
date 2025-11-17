#WAP to pop,del,popitem,append within the dictionary
d={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    p=input("Enter the key as String= ")
    d[p]=int(input("Enter the No. = "))
print(d)
x=input("Enter the Key to be deleted(string) = ")
d.pop(x)
print(d)
d.popitem()
print(d)
y={1:['ritu','megha'],2:['sonali','anu'],3:['maity','puskar']}
a=input("Enter the String = ")
y[3].append(a)
print(y)