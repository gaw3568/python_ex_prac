# 챌린지 문제
# 4가지의 랜덤한 색상을 맞추는 문제

import random

def choice_color():
    color_1 = random.choice(color_list)
    color_2 = random.choice(color_list)
    color_3 = random.choice(color_list)
    color_4 = random.choice(color_list)
    choice_colors = [color_1, color_2, color_3, color_4]
    return choice_colors

def guess_color():
    while True:
        g_color_1 = str.lower(input("Enter a color_1 : "))
        if g_color_1 not in color_list:
            print("There is no color in color list. Try again")
        elif g_color_1 in color_list:
            break

    while True:
        g_color_2 = str.lower(input("Enter a color_2 : "))
        if g_color_2 not in color_list:
            print("There is no color in color list. Try again")
        elif g_color_2 in color_list:
            break

    while True:
        g_color_3 = str.lower(input("Enter a color_3 : "))
        if g_color_3 not in color_list:
            print("There is no color in color list. Try again")
        elif g_color_3 in color_list:
            break

    while True:
        g_color_4 = str.lower(input("Enter a color_4 : "))
        if g_color_4 not in color_list:
            print("There is no color in color list. Try again")
        elif g_color_4 in color_list:
            break

    guess_colors = [g_color_1, g_color_2, g_color_3, g_color_4]
    return guess_colors

def try_guess(choice_colors, guess_colors):
    correct = 0
    wrong = 0

    if guess_colors[0] == choice_colors[0]:
        correct += 1
    elif guess_colors[0] == choice_colors[1] or guess_colors[0] == choice_colors[2] or guess_colors[0] == choice_colors[3]:
        wrong += 1

    if guess_colors[1] == choice_colors[1]:
        correct += 1
    elif guess_colors[1] == choice_colors[0] or guess_colors[1] == choice_colors[2] or guess_colors[1] == choice_colors[3]:
        wrong += 1

    if guess_colors[2] == choice_colors[2]:
        correct += 1
    elif guess_colors[2] == choice_colors[0] or guess_colors[2] == choice_colors[1] or guess_colors[2] == choice_colors[3]:
        wrong += 1

    if guess_colors[3] == choice_colors[3]:
        correct += 1
    elif guess_colors[3] == choice_colors[0] or guess_colors[3] == choice_colors[1] or guess_colors[3] == choice_colors[2]:
        wrong += 1
    
    print("Correct color in the correct place :", correct)
    print("Correct color but in the wrong place :", wrong)
    print()
    return correct

def main():
    choice_colors = choice_color()
    print(choice_colors)
    try_number = 0

    while True:
        guess_colors = guess_color()
        correct = try_guess(choice_colors, guess_colors)
        try_number += 1
        if correct == 4:
            break
    print("You assemble all of 4 colors. Your trying number is",try_number)
    print()

color_list = ["red", "blue", "green", "purple", "navy", "yellow"]
main()