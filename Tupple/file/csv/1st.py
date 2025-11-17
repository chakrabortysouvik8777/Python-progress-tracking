import csv
# Reading a CSV file
x=input("Enter the File Name = ")
with open(x, mode='r') as file:
    a = csv.reader(file)
    header = next(a)  # Skip the header row
    print(header)
    for i in a:
        print(i)