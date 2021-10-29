import csv

file = list(csv.reader(open("Books.csv")))
new_list = []

for row in file:
    new_list.append(row)

del_row = int(input("Enter a delete row : "))
del new_list[del_row]

x = 0
for row in new_list:
    display = x, new_list[x]
    print(display)
    x += 1

revise_row = int(input("Enter a revising row : "))

x = 0
for row in new_list[revise_row]:
    display = x, str(new_list[revise_row][x]).strip()
    print(display)
    x += 1

revise_col = int(input("Enter a revising col : "))
revise_data = input("Enter a revising data : ")
new_list[revise_row][revise_col] = revise_data
print(new_list[revise_row])

with open("Books.csv", "w") as file:
    for row in new_list:
        new_data = row[0] + "," + row[1] + "," + row[2] + "\n"
        file.write(new_data)
