with open("Books.csv", "a") as file:
    count_record = int(input("Enter the counting records : "))

    for i in range(count_record):
        title = input("Enter a title : ")
        author = input("Enter a author : ")
        year = input("Enter a year : ")
        new_record = title + ", " + author + ", " + year + "\n"

        file.write(new_record)

with open("Books.csv", "r") as file:
    find_author = input("Who wants to find person ? ")
    count = 0
    for row in file:
        if find_author in row:
            print(row)
            count += 1
    if count == 0:
        print("Incorrect")        