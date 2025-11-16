#wap to print sum and average of 1st 10 numbers using while loop
n=int(input("Enter the range= "))
s=0
i=0
while i<n:
    s=s+i
    avg=s//n
    i+=1
print(s)  
print(avg)          