import csv

file = open("Stars.csv", "r")
reader = csv.reader(file)

# list() 선언
rows = list(reader)

print(rows[0])