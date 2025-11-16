#wap to generate calender of a month given the start day and number of days in that month
n=input("Enter the month =" )
s=int(input("Enter the number of days ="))
print("                 ",n)
day=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
for i in day:
    print(i,end="    ")
print()
for i in range(1,s+1):
    if i<10:
        print(0,end="")
        print(i,end="     ")
    else:
        print(i,end="     ")    
   # print(i,end=" ")
    if  i%7==0:
        print()
        