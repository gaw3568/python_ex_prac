import csv, random

def make_quiz(num1, num2):
    sentence = str(num1) + " + " + str(num2) + " = "
    return sentence

def save_record(name, question_1, answer_1, count):
    with open("Math Quiz Result.csv","a") as file :
        record = name + ", " + question_1 + str(answer_1) + ", Total score : " + str(count) + "\n"
        file.write(str(record))

count = 0

name = input("Enter your name : ")
print("Math Quiz First")
num1 = random.randint(10,100)
num2 = random.randint(10,100)
correct_result_1 = num1 + num2

question_1 = make_quiz(num1, num2)
answer_1 = int(input(question_1))

if answer_1 == (correct_result_1):
    count += 1

save_record(name, question_1, answer_1, count)

print("Math Quiz Second")
num1 = random.randint(10,100)
num2 = random.randint(10,100)
correct_result_2 = num1 + num2

question_2 = make_quiz(num1, num2)
answer_2 = int(input(question_2))

if answer_2 == (correct_result_2):
    count += 1

save_record(name, question_2, answer_2, count)