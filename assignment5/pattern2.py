'''*****
   ****
   ***
   **
   *
   '''
n=int(input('Enter rhe range ='))
for i in range(1,n+1): 
   for j in range(i,n+1):
        if j==n:
           print(" *")
        else :
           print(" *",end=" ")    