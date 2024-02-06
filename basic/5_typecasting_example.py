birth_year = input("What's your birth year ? ")
# age = 2023 - birth_year  # normally, we get error

# because what ever you enter using input fn , the data is stored as string data type
# so "birth_year" is string data type

# so we need typecasting;
# int(birth_year)  # The input is converted into interger
age = 2023 - int(birth_year)
print("age = ", age)
