## random 함수를 사용한 6개의 로또 번호 생성 예제
import random

new_list = []

while len(new_list) <= 6:
    num = random.randint(1,45)
    if num in new_list:
        continue
    else:
        new_list.append(num)

print(sorted(new_list))

a,b = map(int, input("enter : ").split())
print(a + b)