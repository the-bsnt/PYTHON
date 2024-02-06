high_income = True
high_credit = False

# logical AND
if high_income and high_credit:
    print("the person is eligible for loan")

# logical OR
if high_income or high_credit:
    print("person can be given loan with certain conditions")
else:
    print("the person is not eligible for loan")

# logical NOT

statement = False
if not statement:  # now the bellow code is executed if condition will be  false;
    print("the statement is false")
