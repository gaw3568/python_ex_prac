foods = {}

for i in range(4):
    favorite_foods = input("Enter a food : ")
    foods[i+1] = favorite_foods

print(foods)

remove_item = input("What do you want to remove item ? ")
del foods[int(remove_item)]

print(sorted(foods.values()))