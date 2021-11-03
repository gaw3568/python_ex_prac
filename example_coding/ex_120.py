import random
from typing import AnyStr

print("1) Addition")
print("2) Subtraction")
print("Enter 1 or 2: ")

def first():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    correct_num = num1 + num2
    answer = int(input(str(num1)+ " + " + str(num2) + " = "))
    # correct_num, answer 두 변수를 return 하는 것과 
    # correct_num, answer 두 변수를 새로운 변수에 저장해서 return 하는 것의 차이점? (코드를 깔끔하게 하기 위한 것인지?) 
    # sentence = (correct_num, answer)
    # return sentence
    return correct_num, answer

def second():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    correct_num = num1 - num2
    answer = int(input(str(num1)+ " - " + str(num2) + " = "))
    return correct_num, answer

def check(correct, answer):    
    if correct == answer:
        print("Correct")
    elif correct != answer:
        print("Incorrect, the answer is", correct)

def main():
    menu = int(input("Enter a menu option : "))
    if menu == 1:
        correct, answer = first()
        check(correct, answer)
    elif menu == 2:
        correct, answer = second()
        check(correct, answer)
    else:
        print("Enter a correct menu option!")    



main()