import random
random_number = random.randint(1,100)

number = int(input("Enter a number : "))
count = 1


while number != random_number:
    if number < random_number:
        print(number, "is lower than random_number")
        number = int(input("Enter a number : "))
        count += 1

    if number > random_number:
        print(number, "is higher than random_number")
        number = int(input("Enter a number : "))
        count += 1

print("Well done,","random_number is",random_number,"\nyou took \"" + str(count)+ "\" attempts")