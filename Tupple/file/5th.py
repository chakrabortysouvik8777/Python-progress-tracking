p=open("C:/fdrive/B.Tech 1st sem 1st batch 2024-25/Python 2/13.11.25/file/Dip.txt","a")        
p.write("\nAmi Chucho.")
p.close()
p=open("C:/fdrive/B.Tech 1st sem 1st batch 2024-25/Python 2/13.11.25/file/Dip.txt","r")     
for i in p.readlines():
    print(i,end='')
p.close()