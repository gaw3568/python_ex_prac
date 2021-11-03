
compnum = 50
number = int(input("Enter a number : "))
count = 1


while number != compnum:
    if number < compnum:
        print(number, "is lower than compnum")
        number = int(input("Enter a number : "))
        count += 1

    if number > compnum:
        print(number, "is higher than compnum")
        number = int(input("Enter a number : "))
        count += 1

print("Well done,","compnum is",compnum,"\nyou took \"" + str(count)+ "\" attempts")