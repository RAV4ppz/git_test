name = input("What is your name? ")
birth_year = input("What is your birth year? ")
age = 2022 - int(birth_year)

print("Welcome",name,"You are",age,"years old")

patient = input("Are you a new patient? ")
if patient == ("yes"):
    print("You are a new patient!")
elif patient == ("no"):
    print("You are a returning patient!")
