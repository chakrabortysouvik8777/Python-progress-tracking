'''  *
   *   *
 *   *   * '''
n=int(input('Enter rhe range ='))
for i in range(1,n+1): 
    for sp in range(n,i,-1):
        print(" ",end=" ")
    for j in range(i,i+1):
        if i==j:
                print(" *")
        else:
                print(" *",end="")    
