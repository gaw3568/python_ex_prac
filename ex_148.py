# 챌린지 문제
# ID, password 생성

import csv

def Get_csv():
    file = list(csv.reader(open("User_info.csv")))
    new_list = []
    for i in file:
        new_list.append(i)
    return new_list

def Create_id(temp_list):
    while True:
        new_ID = input("Enter a new ID : ")
        if new_ID in temp_list:
            print(new_ID + " is already existing in file. Try again")
        else:
            break
    return new_ID    
                
def Create_pw():
    special_font_list = ["!", "@", "#", "$", "%", "&", "<", "?", ">"]
    number_list = ["1","2","3","4","5","6","7","8","9","0"]
    new_PW = input("Enter a new Password : ")
    while True:
        score = 0
        check_low = False
        check_up = False
        check_sf = False
        check_num = False

        for i in new_PW:
            if i.islower():
                check_low = True
            if i.isupper():
                check_up = True
            if i in special_font_list:
                check_sf = True
            if i in number_list:
                check_num = True

        if check_low:
            score += 1
        if check_up:
            score += 1
        if check_sf:
            score += 1
        if check_num:
            score += 1
        if len(new_PW) >= 8:
            score += 1

        if 1 <= score <= 2:
            print("Your password is very weak. Try again")    
        elif 3 <= score <= 4:
            print("This password could be improved")
            answer = str.lower(input("Do you want to reenter password ? (y / n) : "))
            if answer == 'n':
                break
        if score == 5:
            print("Your password is very powerful")
            break
    return new_PW  

def Change_pw(temp_list):
    user_ID = input("Enter a user ID : ")
    for row in temp_list:
        if user_ID in row[0]:
            new_pw = Create_pw()
            location = user_ID.index(user_ID)
            temp_list[location][1] = new_pw

            with open("User_info.csv", "w") as file:
                for n in temp_list:
                    record = n[0] + "," + n[1] + "\n"
                    file.write(str(record))
        else:
            print("There is not user ID in the list. Try again")

def Display_all(temp_list):
    for x in temp_list:
        print(x[0])

def main():
    print("1) Create csv file")
    print("2) Use csv file what is existing in folder")
    check = int(input("Enter a 1) or 2) : "))
    print()
    if check == 1:
        with open("User_info.csv", "w") as file:
            print("File is created")
    elif check == 2:
        while True:
            print("1) Create a new User ID")
            print("2) Change a password")
            print("3) Display all User IDs")
            print("4) Quit")
            print()

            temp_list = Get_csv()
            menu_option = int(input("Enter Selection : "))

            if menu_option == 1:
                new_ID = Create_id(temp_list)
                new_PW = Create_pw()
                with open("User_info.csv", "a") as file:
                    record = new_ID + "," + new_PW + "\n"
                    file.write(str(record))
                print()
            elif menu_option == 2:
                Change_pw(temp_list)
                print("Password is changed")
                print()
            elif menu_option == 3:
                Display_all(temp_list)
                print()
            elif menu_option == 4:
                print("Program is quit")
                break
            else:
                print("Enter correct menu option. Try again")
main()