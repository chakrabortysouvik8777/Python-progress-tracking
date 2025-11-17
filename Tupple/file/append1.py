#(append)WAP to add/edit new content within the previously created file or if the file is not created it will create a  new file
p=input("Enter the Path = ")
x=input("Enter the File Name = ")
r=open(p+x,"a")
a=input("Enter the Sentence = ")
r.write(a)
r.write("\n")
a=input("Enter the 2nd Sentence = ")
r.write(a)
r.close()
r=open(p+x,"r")
print(r.read())
r.close()








