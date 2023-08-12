#
# if condition:
#     do this work
# else:
#     do this

print("Welcome to the rollerCoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0
if height > 120:
    print("you can ride")
    if age > 18:
        bill = 300
        print("You hava to pay Rs 300")
    elif age > 12 & age < 18:
        bill = 200
        print("You have to pay Rs 200")
    elif age > 45 & age < 55:
        bill = 0
        print("You don't have to pay")
    else:
        bill = 150
        print("You have to pay Rs 150")
    want_photo = input("Do you want a photo taken? Y or N.")
    if want_photo == "Y":
        bill += 50
    print(f"Your final bill is {bill}")

else:
    print("Sorry, You have to grow taller before you can ride.")
