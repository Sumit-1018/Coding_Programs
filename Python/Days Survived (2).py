from datetime import date
birth_date = input("Enter Birthdate(DD/MM/YYYY):")

a = int(birth_date.split('/')[0])
b = int(birth_date.split('/')[1])
c = int(birth_date.split('/')[2])

current_date = input("Enter Current date(DD/MM/YYYY):")

d = int(current_date.split('/')[0])
e = int(current_date.split('/')[1])
f = int(current_date.split('/')[2])

birth_date = date(c, b, a)
current_date = date(f, e, d)
survived = current_date - birth_date
print("Days survived:",survived.days)
