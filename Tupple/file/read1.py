#WAP to print the content of the file 
p=input("Enter the Path = ")
x=input("Enter the File Name = ")
r=open(p+x,"r")
print(r.read())
r.close()