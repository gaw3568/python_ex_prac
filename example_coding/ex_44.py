number = int(input("How many people invite to the party ? "))

if number < 10:
    name = input("What's your name : ")
    
    for i in range(number):
        print(name + " has been invited")
elif number >= 10:
    print("Too many people")