from array import *
import random

arr_1 = array('i', [])
arr_2 = array('i', [])

for i in range(3):
    number_1 = int(input("Enter a number : "))
    arr_1.append(number_1)

for i in range(5):
    number_2 = random.randint(1,100)
    arr_2.append(number_2)

## 배열 2개를 합칠 경우, extend() 메서드 사용!
arr_1.extend(arr_2)

arr_1 = sorted(arr_1)

for i in arr_1:
    print(i)