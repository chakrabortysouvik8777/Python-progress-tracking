# WAP to take manual input within a dictionary & print the dictionary
x={1:"chandan",2:"debojit",3:"meeraj",4:"mora",2:"puskar",5:"satyam",6:"chandan"}
print("Dictionary = ",x)
for k,v in x.items():
    print(k,":",v)

for k in x.keys():
    print(k,end=' ')
print()

for v in x.values():
    print(v,end=' ')
