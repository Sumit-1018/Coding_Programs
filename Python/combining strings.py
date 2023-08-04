keys=(input("keys:").split(","))
l=[]
for i in range(len(keys)):
    values=input("values:").split(",")
    l.append(values)
d=dict(zip(keys,l))
print(d)
for row in zip(*([key]+(value) for key,value in sorted(d.items()))):
    print(*row)