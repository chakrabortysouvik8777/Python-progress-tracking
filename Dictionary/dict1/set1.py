#implement set operation  union,intersection,difference
s1=set()
s2=set()
s3=set()
n =int(input("Enter the Range = "))
for i in range(1,n+1,1):
    s1.add(int(input("Enter the No. for 1st Set= ")))
print("set 1 =",s1)
for i in range(1,n+1,1):
    s2.add(int(input("Enter the No.  for 2nd Set= ")))
print("set 2 =",s2)
s3=s1 | s2
print("Set Union = ",s3)
s3=s1 & s2
print("Set Intersection = ",s3)
s3= s1 - s2
print("Set Difference (s1-s2) = ",s3)
s3= s2 - s1
print("Set Difference (s2-s1)= ",s3)
