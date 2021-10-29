import csv

first_year = int(input("Enter a first year : "))
last_year = int(input("Enter a last year : "))

file = list(csv.reader(open("Books.csv")))
book_list = []

for row in file:
    book_list.append(row)

for row in book_list:
    if int(row[2]) >= first_year and int(row[2]) <= last_year:
        print(row)