 #happy number
n=int(input("enter the number="))
s=0
while(n>0):
     r=n%10
     n=n//10
     s=s+r**2
     if n==0:
         if s==1:
          print("happy number")
         exit()
     elif s!=1 and s<10:
        break
     else:
   # n=s
    #s=0
        print("not a happy number")
             