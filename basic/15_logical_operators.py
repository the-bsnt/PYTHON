temp = input("What is the temperature of surrounding?")
temp = int(temp)
if temp >= 35:
    print("It's a hot day ")
elif temp <= 15:
    print("It's a cold day ")
else:
    print("It's a warm day (neither hot nor cold).")
