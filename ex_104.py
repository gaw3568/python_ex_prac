list = {}

for i in range(4):
    name = input("Enter a name : ")
    age = int(input("Enter a age : "))
    shoe_size = int(input("Enter a shoe size : "))

    list[name] = {"age":age, "shoe_size":shoe_size}

delete_name = input("Enter a name who wants to delete : ")
del list[delete_name]

for name in list:
    print(name, list[name]["age"], list[name]["shoe_size"])