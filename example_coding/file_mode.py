def file_mode():
    file_name = (input("Enter a file name : "))
    file_option = str.lower(input("Enter a file option : "))
    
    isError = True

    if file_option == 'w' or file_option == 'r' or file_option == 'a': 
        newFile = open(file_name, file_option)
        return newFile
    else:
        print("There are no options in file options")
        return isError