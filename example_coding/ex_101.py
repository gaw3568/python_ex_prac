sales_dic = {"John": {"N":3056, "S":8463, "E":8441, "W":2694}, 
"Tom":{"N":4832, "S":6786, "E":4737, "W":3612}, 
"Anne":{"N":5239, "S":4802, "E":5820, "W":1859}, 
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

name = input("Enter a name : ")
region = input("Enter a region : ")

print(sales_dic[name][region])

new_sales = int(input("Enter a new sales : "))

sales_dic[name][region] = new_sales

print(sales_dic[name])

