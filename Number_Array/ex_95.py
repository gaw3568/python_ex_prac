from array import *
import random

def input_func():
    number = int(input("Enter a number : "))
    return number


arr = array("f", [35.04, 22.91, 91.41, 85.51, 33.72])

while True:
    number = input_func()
    
    if 2 > number or number > 5:
        print("Error")
        number = input_func()

    else:
        for i in arr:
            i = i / number
            ## 소수점 2자리까지만 출력되도록 round() 반올림 메서드 사용
            print(round(i,2))
        break    
            
        
