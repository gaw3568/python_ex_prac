import random

random_answer = random.choice(['h','t'])
choose_answer = str.lower(input())

if random_answer == choose_answer:
    print("You win")
else:
    print("Bad luck")
    print("Computer's choice is", random_answer)