#update()
x={'name':'mainak','class':'xii','sub':'cs','marks':00}
x.update({'marks':45})
print(x)
x.update({'age':17})
print(x)
for k,v in x.items():
    print(k,":",v)