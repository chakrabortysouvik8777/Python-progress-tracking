#wap to find out the GCD and LCM of 2 number
x=int(input("enter the 1st number= "))
y=int(input("enter the 2nd number= "))
i=1
while i<=x:
    if x%i==0 and y%i==0:
        gcd=i
    i+=1
print("gcd is =",gcd)
lcm=(x*y)/gcd
print("lcm is =",lcm)        
        