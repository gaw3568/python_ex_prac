from array import *

num_arr = array('i', [])

for i in range(5):
    number = int(input("Enter : "))
    num_arr.append(number)

num_arr = sorted(num_arr)
num_arr.reverse()
print(num_arr)    