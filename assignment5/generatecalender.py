#wap to generate calender of a month given the start day and number of days in that month
n=input("Enter the month =" )
d=int(input("Enter the number of days ="))
s=int(input("Enter the starting day ="))
print("\t\t",n)
print("\nSUN\tMON\tTUE\tTHU\tFRI\tSAT\n")
day=1
for i in range(1,s+1):
    print("\t",end="")
print(day,end="\t")  
day+=1
s+=1  
for i in range(day,d+1):
    if s==0:
        s=0
        print()
    print(i,end="\t")
    s+=1