from file_mode import file_mode

file_name = input("Enter a file name : ")
file_option = input("Enter a file option : ")

file = file_mode(file_name, file_option)

file.write("John\n")
file.write("Sancho\n")
file.write("Mata\n")
file.write("Herrera\n")
file.write("Rooney\n")
file.close()