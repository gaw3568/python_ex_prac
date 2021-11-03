import random

number = int(input("Enter a number : "))
random_number = random.randint(1,10)

while number != random_number:
    print("Wrong, please enter a number again")
    number = int(input("Enter a number again : "))

print("Correct")