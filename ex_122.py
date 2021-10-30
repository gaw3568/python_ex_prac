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

def main():
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()

    while True:
        menu = int(input("Enter a menu option : "))
        if menu == 1:
            add()
        elif menu == 2:
            show_all()
        elif menu == 3:
            print("Program is quit")
            break

main()