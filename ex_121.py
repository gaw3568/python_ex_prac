# 1. 목록의 이름을 추가하는 메뉴
# 2. 목록의 이름을 수정하는 메뉴
# 3. 목록의 이름을 삭제하는 메뉴
# 4. 목록의 모든 이름을 표시하는 메뉴
# 5. 프로그램을 졸료하는 메뉴

def add():
    name = input("Enter a name to input : ")
    name_list.append(name)
    return name_list

def revise():
    index = 0
    for i in name_list:
        print(index, i)
        index += 1

    revise_index = int(input("Enter a index to revise : "))
    new_name = input("Enter a name to revise : ")
    name_list[revise_index] = new_name
    return name_list

def delete():
    index = 0
    for i in name_list:
        print(index, i)
        index += 1

    delete_index = int(input("Enter a index to delete : "))
    del name_list[delete_index]
    return name_list

def show():
    for i in name_list:
        print(i)
    print()    

def menu():
    print("1) Add name")
    print("2) Revise name")
    print("3) Delete name")
    print("4) Show all name")
    print("5) Quit")
    print()

def main():
    while True:
        menu()
        menu_option = int(input("Enter a menu option : "))
        
        if menu_option == 1:
            name_list = add()
            print()
        elif menu_option == 2:
            name_list = revise()
            print()
        elif menu_option == 3:
            name_list = delete()
            print()
        elif menu_option == 4:
            show()    
        elif menu_option == 5:
            print("Program is quit")
            break
        else:
            print("Select a correct menu option!")
            print()

name_list = []
main()