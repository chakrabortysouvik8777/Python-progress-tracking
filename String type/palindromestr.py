#palindrome string
x= input("enter the string=")
y=x[::-1]
print(y)
if x.lower()==y.lower():
    print("palindrome string")
else:
        print("not palindrome string")