with open("Books.csv","r") as file:
    row = 0
    for line in file:
        print(row, ":", line)
        row += 1