import datetime

now = datetime.datetime.now()
birth_year = input("What is your birth year? ")
print(now.year - int(birth_year))

# or
# now = datetime.datetime.now()
# birth_year = input("What is your birth year? ")
# age = now.year - int(birth_year)
# print(age)