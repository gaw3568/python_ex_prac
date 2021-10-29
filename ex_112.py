import csv
file = open("Books.csv","a")

title = input("Enter a title : ")
author = input("Enter a author : ")
year = input("Enter a year : ")
new_record = title + ", " + author + ", " + year + "\n"

file.write(str(new_record))
file.close()

file = open("Books.csv","r")

for line in file:
    print(line)
file.close()
