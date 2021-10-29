from file_mode import file_mode

file = file_mode()

if file == True:
    print("Error")
else:
    file.write("De gea\n")
    file.close()

file = file_mode()

if file == True:
    print("Error")
else:
    print(file.read())
