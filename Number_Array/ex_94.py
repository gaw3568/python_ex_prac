from array import *

arr = array("i", [1,2,3,4,5])

for i in arr:
    print(i)

while True:
    number = int(input("Enter a number : "))

    if number not in arr:
        number = int(input("Enter a number again : "))

    elif number in arr:
        print(arr.index(number))
        break
