r=open("C:/fdrive/B.Tech 1st sem 1st batch 2024-25/Python 2/13.11.25/file/Dip.txt","w")      
x=input("Enter the Sentence= ")
r.write(x)
r.write("\n")
y=input("Enter the 2nd Sentence= ")
r.write(y)
r.close()
r=open("C:/fdrive/B.Tech 1st sem 1st batch 2024-25/Python 2/13.11.25/file/Dip.txt","r")            
print(r.read())
r.close()











