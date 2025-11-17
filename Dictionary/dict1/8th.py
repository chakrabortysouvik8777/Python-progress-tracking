#WAP to even element store within the list & then delete 
d={}
li=[]
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    d[i]=int(input("Enter the No. = "))
print(d)
for k,v in d.items():
    if v%2==0:
        li.append(d[k])
print(li)
li.clear()
print(li)
    

