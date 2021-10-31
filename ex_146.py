# 챌린지 문제
# Shift code, Reverse shift code 기능을 갖춘 인코딩,디코딩 문제

alphabet_list = ['a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t',
                'u','v','w','x','y','z',' ']

def menu():
    print("1) Make a code")
    print("2) Decode a message")
    print("3) Quit")
    print()

def make():
    code = str.lower(input("Enter a code : "))
    shift_number = int(input("Enter a shift number : "))
    return code, shift_number

def shift(code, number):
    new_code = ""

    for i in code:
        x = alphabet_list.index(i)
        x += number

        if x > 26:
            x -= 27
        new_code += alphabet_list[x]
    print(new_code)    
    print()

def decode(code, number):
    new_code = ""
    for i in code:
        x = alphabet_list.index(i)
        x -= number
        
        if x < 0:
            x += 27
        new_code += alphabet_list[x]
    print(new_code)    
    print()

def main():
    while True:
        menu()
        menu_option = int(input("Enter your selection : "))
        if menu_option == 1:
            code, shift_number = make()
            shift(code, shift_number)
        elif menu_option == 2:
            code, r_shift_number = make()
            decode(code, r_shift_number)
        elif menu_option == 3:
            print("Program is quit")
            break
        else:
            print("Incorrect menu option")

main()