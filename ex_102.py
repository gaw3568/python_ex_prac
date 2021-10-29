list = {}

for i in range(4):
    name = input("Enter a name : ")
    age = int(input("Enter a age : "))
    shoe_size = int(input("Enter a shoe size : "))

    list[name] = {"age":age, "shoe_size":shoe_size}

name = input("Enter a name : ")
print(list[name])