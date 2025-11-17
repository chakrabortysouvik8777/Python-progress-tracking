#WAP to even key store from the dictionary to the list
d={}
li=[]
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    d[i]=int(input("Enter the No. = "))
print(d)
for k,v in d.items():
    if k%2==0:
        li.append(d[k])
print(li)    

