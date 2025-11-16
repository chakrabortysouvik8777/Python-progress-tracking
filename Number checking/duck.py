#duck number
'''n=int(input("enter the number = "))
f=0
if n[0]=='0':
    print("not duck number")
else:
    for i in n:
        if i==0:
            f==1
            break
if f==1:
    print("duck number")
else:
    print("not Duck")  '''
    
n= int(input("enter the number = "))
m=n
c=0
while m!=0:
     d=m%10
     c+=1
     m=m//10
if c>0:
        print("duck number ") 
else:
       print("not duck number")      
    
    