from array import *

arr = array('i', [])
arr_2 = array('i', [])

for i in range(5):
    number = int(input("Enter a number : "))
    arr.append(number)

arr = sorted(arr)
print(arr)

new_number = int(input("Enter a new number in the range of array : "))

if new_number in arr :
    arr.remove(new_number)
    arr_2.append(new_number)
    print(arr)
    print(arr_2)
else:
    print("There is not new number in the array!")