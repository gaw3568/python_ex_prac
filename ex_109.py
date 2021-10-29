from file_mode import file_mode

print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
print("Make a selection 1, 2 or 3 : ", end="")

menu = int(input())

if menu == 1:
    file = file_mode()
    subject = input("Enter a subject name : ")
    file.write(subject+"\n")
    file.close()
elif menu == 2:
    file = file_mode()
    print(file.read())
elif menu == 3:
    file = file_mode()
    subject = input("Enter a subject name : ")
    file.write(subject+"\n")
    file.close()

    file = file_mode()
    print(file.read())
else:
    print("Error")    