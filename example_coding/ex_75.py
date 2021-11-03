threehundred_number = [301,999,502,781]
for i in threehundred_number:
    print(i)

number = int(input("Enter a number : "))

if number in threehundred_number:
    print(threehundred_number.index(number))
else:
    print("That is not in the list")    