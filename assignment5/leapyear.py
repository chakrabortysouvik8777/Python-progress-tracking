#wap to displays all leap year from 1900-2025
n=int(input("enter the range= "))
i=1900
for i in range(1900,n+1,1):
    if  i%400==0 :
        print("leap year",i)
    elif i%4==0 and i%100!=0:
        print("leap year",i)
    else:
        print("not leap year",i)