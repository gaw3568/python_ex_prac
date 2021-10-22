import random

# random_number = random.randint(1,10)
# number = int(input("Enter a number : "))

# while number != random_number:
#     if number < random_number:
#         print("It is too lower than random number")
#         print("please enter a number again")
#         number = int(input("Enter a number again : "))
#     elif number > random_number:
#         print("It is too higher than random number")
#         print("please enter a number again")
#         number = int(input("Enter a number again : "))

# print("Correct")

random_number = random.randint(1,10)

while True:
    number = int(input("Enter a number : "))
    if number == random_number:
        break
    elif number < random_number:
        print("It is too lower than random number")
        print("please enter a number again")
    elif number > random_number:
        print("It is too higher than random number")
        print("please enter a number again")

print("Correct")