import csv

def add():
    with open("Salaries.csv","a") as file:
        name = input("Enter a name : ")
        salary = input("Enter the salary : ")
        record = name + ", " + salary + "\n"
        file.write(str(record))
    print()    

def show_all():
    file = csv.reader(open("Salaries.csv"))

    for row in file:
        print(row)
    print()    

def delete():
    file = csv.reader(open("Salaries.csv"))
    copy_list = []

    for row in file:
        copy_list.append(row)

    index = 0
    for i in copy_list:
        print(index, i)
        index += 1

    delete_index = int(input("Enter a index to delete : "))
    del copy_list[delete_index]

    with open("Salaries.csv", "w") as new_file:
        for row in copy_list:
            record = row[0] + ", " + str(row[1]).strip() + "\n"
            new_file.write(str(record))

def main():
    while True:
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete a record")
        print("4) Quit program")
        print()

        menu = int(input("Enter a menu option : "))
        if menu == 1:
            add()
        elif menu == 2:
            show_all()
        elif menu == 3:
            delete()
        elif menu == 4:
            print("Program is quit")
            break

main()