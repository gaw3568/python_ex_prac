answer = input("Do you want to invite people in the party? (y/n) ")
count = 0

while answer == 'y' or answer == 'yes':
    name = input("Enter the name who invite : ")
    print(name + " has now been invited")
    count += 1
    answer = input("Do you want to invite people in the party? (y/n) ")

print(count)    
