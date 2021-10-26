from array import *
import random

int_arr = array('i', [])

for i in range(5):
    random_num = random.randint(0,100)
    int_arr.append(random_num)

for i in int_arr:
    print(i)    