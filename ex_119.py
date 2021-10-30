import random

def correct_num():
    low_num = int(input("Enter a low number : "))
    high_num = int(input("Enter a high number : "))
    comp_num = random.randint(low_num, high_num)
    return comp_num

def thinking_num():
    print("I am thinking of a number...")
    user_think_num = int(input("Enter a number what you think : "))
    return user_think_num

def check_num(comp_num, user_num):
    while True:
        if user_num == comp_num:
            print("Correct, you win")
            break
        elif user_num < comp_num:
            user_num = int(input("It is too low number. Try again : "))
        elif user_num > comp_num:
            user_num = int(input("It is too high number. Try again : "))

def main():
    comp_num = correct_num()
    user_num = thinking_num()
    check_num(comp_num, user_num)

main()