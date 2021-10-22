total = 0
for i in range(5):
    num = int(input("enter a number : "))
    answer = input("do you want to sum number and total? (y/n) ")

    if answer == 'y' or 'yes':
        total += num

print(total)            
