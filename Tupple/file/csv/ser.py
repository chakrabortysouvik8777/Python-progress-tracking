#5) Write a python program to demonstrate the use of {m,n} regular expression. 
import re 
string=input("Enter the string: ")
ser_str = r"be{0,10}" 
output = re.findall(ser_str, string) 
print(output)