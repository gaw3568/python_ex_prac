from array import *

int_arr = array('i',[])

while len(int_arr) < 5:
    number = int(input("Enter a number : "))
    
    if 10 <= number <= 20:
        int_arr.append(number)
    else:
        print("Outside the range")

    if len(int_arr) == 5:
        int_arr = sorted(int_arr)

for i in int_arr:
    print(i)