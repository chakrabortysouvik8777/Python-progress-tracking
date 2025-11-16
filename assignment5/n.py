'''         *           *   
           * *         * *
          * * *       * * *
         * * * *     * * * *
        * * * * *   * * * * * 
      * * * * * * * * * * * *
       * * * p y t h o * * * 
        * * * * * * * * * *
         * * * * * * * * *
          * * * * * * * *
           * * * * * * *
            * * * * * *
             * * * * *
              * * * *
               * * *
                * *
                 *'''
num=int(input("enter the range ="))
m=input("enter the string =")
l=len(m)
n=num//2
for i in range(n):
    print(" *"*(n-i-1)+"* "*(i+1),end="")
    if num%2==0:
        for j in range(2*(n-i-1)):
            print(" ",end="")
    else:
        for j in range(2*(n-i-1)+1): 
            print(" ",end="") 
    for j in range(i+1):
        print("* ",end="")          
    print()
       
if num%2==0:
    if l%2==0:
        print("* "*((num-1)//2) + " ".join(m) + " *"*((num-1)//2))
    else:
        print("* "*((num-1)//2) + " ".join(m) + " *"*(((num-1)//2)))  
else:
   if l%2==0:
        print("* "*((num-1)//2) + " ".join(m) + " *"*(((num-1)//2)+1))
   else:
        print("* "*((num-1)//2) + " ".join(m) + " *"*((num-1)//2))  
     
for i in range(num,0,-1):
    print(" "*(num-i)+"* "*(i))  
          
             
