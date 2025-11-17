#WAP to create a file & print the file content
p=input("Enter the Path = ")
x=input("Enter the File Name = ")
r=open(p+x,"w")
a=input("Enter the Sentence = ")
r.write(a)
r.write("\n")
a=input("Enter the 2nd Sentence = ")
r.write(a)
r.close()
r=open(p+x,"r")
print(r.read())
r.close()






