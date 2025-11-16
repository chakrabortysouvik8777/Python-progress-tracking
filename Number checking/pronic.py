#pronic number
n=int(input("enter the number "))
s=0
for i in range(1,n+1):
    if i*(i+1)==n:
        s=1
        break
    if s==1:
        print("pronic number")
    else:
        print("not pronic") 
