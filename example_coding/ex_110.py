from file_mode import file_mode

file = file_mode()

name = str.title(input("Enter a name in the list : "))
name += "\n"

for row in file:
    if row != name:
        file2 = file_mode()
        name = row
        file2.write(name)
        file2.close()

file.close()

