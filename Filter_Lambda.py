## filter() 함수, lambda() 함수 사용 예제
## 리스트 내의 음수를 제외한 양수의 값만 출력하기

def positive_num(x):
    if (x > 0):
        return x

print("filter() 함수 및 lambda() 함수 이용 예제")
list_ = [1, -2, 3, -5, 8, -3]
print(list(filter(positive_num, list_)))
print(list(filter(lambda x: x > 0, list_)))
print(list(map(lambda x: x * 3, list_)))
print()

print("변환하고자 하는 진법을 사용한 예제")
num = int("0xea", base = 0)
num1 = int('1001', base = 8)
print(num)
print(num1)
print()

print("최댓값, 최솟값 문제")
n_list = [-8, 2, 7, 5, -3, 5, 0, 1]
maxNum = max(n_list)
minNum = min(n_list)
MaxMinSum = max(n_list) + min(n_list)
print(f"maxNum = {maxNum}")
print(f"minNum = {minNum}")
print(f"MaxMinSum = {MaxMinSum}")


print("반올림 함수 사용 예제")
num = 17 / 3
print(round(num, 4))