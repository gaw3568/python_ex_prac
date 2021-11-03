number = int(input("Enter a number "))

while number < 10 or number > 20:
    
    if number < 10:
        print("Too low")
    elif number > 20:
        print("Too high")    

    number = int(input("Enter a number "))

print("Thank you")
