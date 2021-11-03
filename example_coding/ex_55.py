import random
random_number = random.randint(1,5)
number = int(input())

if random_number == number:
    print("Well done")
    
elif random_number > number:
    print("Your choice is too low")
    number = int(input("Enter again : "))

    if random_number == number:
        print("Correct")
    else:
        print("You lose")    

elif random_number < number:
    print("Your choice is too high")    
    number = int(input("Enter again : "))    

    if random_number == number:
        print("Correct")
    else:
        print("You lose")    
