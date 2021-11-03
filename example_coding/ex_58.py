import random
result = 0

for i in range(5):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct_answer = num1 + num2
    print(num1,"+",num2,"= ", end="")
    answer = int(input())

    if answer == correct_answer:
        result += 1

print("\nYour correct answer :", result)