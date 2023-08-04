from datetime import date
birth_date = input("Enter Birthdate(DD/MM/YYYY):")

birth_year = int(birth_date.split('/')[0])
birth_month = int(birth_date.split('/')[1])
birth_date = int(birth_date.split('/')[2])

current_date = input("Enter Current date(DD/MM/YYYY):")

current_year = int(current_date.split('/')[0])
current_month = int(current_date.split('/')[1])
current_date = int(current_date.split('/')[2])

birth_date = date(birth_date, birth_month, birth_year)
current_date = date(current_date, current_month, current_year)
survived = current_date - birth_date
print("Days survived:",survived.days)
