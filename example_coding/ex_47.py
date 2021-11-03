number = int(input("Enter a number1 : "))
number2 = int(input("Enter a number2 : "))
sum = number + number2

answer = str.lower(input("Answer : "))

while answer == 'y' or answer == 'yes':
    new_number = int(input("Enter a number : "))
    sum += new_number
    answer = str.lower(input("Do you want to add new number ? "))

print(sum)