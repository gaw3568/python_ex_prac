import random
colour_list = ["red","blue","green","ivory","violet"]
colour = random.choice(colour_list)

while True:
    user_choice = str.lower(input("Choose your favorite colour : "))

    if user_choice == colour:
        print("Well done")
        break
    else:
        print("I bet you are",colour,"with envy")    