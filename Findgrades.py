# number =(input("Enter your Number : "))
# print(number, type(number))

# number = 44
# if number == "44":
#     print("you are pass")
# else:
#     print("oh! you are fail")

# number = 101
# if number == 100:
#     print("hurry you are pass")
# elif number < 90:
#     print("you are right")
# elif number < 80:
#     print("absolute")
# else:
#     print("Fail")

height = 12
age = 11
education = 10

age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))
education = input("Enter your education: ").lower()

if age < 11 and height < 10:
    print("Acceptable")
elif height < 12 and education < 10:
    print("Acceptable")
elif education < 10 and age < 11:
    prnit("Aceept")
else:
    print("fail")


