#WAP to check whether a string is anagram or not
x=input("enter the 1st string=") 
y=input("enter the 2nd string=") 
f=0
g=0
if len(x)==len(y):
    for i in x:
        if i not in y:
            f=1
            break
    for i in y:
        if i not in x:
            g=1
            break
    if f==0 and g==0:        
        print("anagram string")
    else:
        print("not anagram string")    
else:
    print("not anagram string")    