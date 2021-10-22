name = input()
number = int(input())

if number < 10:
    for i in range(number):
        print(name)
elif number >= 10:
    for i in range(3):
        print("Too high")        