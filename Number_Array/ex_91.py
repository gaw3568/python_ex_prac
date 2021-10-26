from array import *

arr = array('i', [4,9,13,4,1])

print(arr)

check_number = int(input("Enter the finding number : "))
count = 0

for i in range(len(arr)):
    if check_number == arr[i]:
        count += 1

print("Total counting :",count)        