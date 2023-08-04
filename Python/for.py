import pickle
class emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def dis(self):
        print(self.id,self.name,self.sal)
f=open("emp.dat","wb")
n=int(input("how many employee?"))
for i in range(n):
    id=int(input('enter id: '))
    name=input('enter name: ')
    sal=float(input('enter salary: '))
    e=emp(id,name,sal)
    pickle.dump(e,f)
f.close()
f=open("emp.dat","rb")
d=pickle.load(f)
print(d)