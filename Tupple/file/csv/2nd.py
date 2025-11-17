import csv
# Writing to a CSV file
data = [
    ['Name', 'Age', 'Address'],
    ['Debojit gangster', 18, 'Salt Lake'],
    ['Sayanjit Culprit1', 20, 'Baguiati'],
    ['Trishan Culprit2', 17, 'lake Town']
]
print(data)
x=input("Enter the File name = ")
with open(x, mode='w', newline='') as file:
    p = csv.writer(file)
    p.writerows(data)
print("File created Successfully!!!!")