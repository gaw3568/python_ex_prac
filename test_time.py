## time 모듈을 사용해 현재 날짜와 시간을 나타내는 예제
import time

result = time.time()
result_1 = time.localtime(result)

## asctime과 ctime은 동일한 결과를 나타냄
result_2 = time.asctime(result_1)
result_3 = time.ctime()
print(type(result_2))
print(result_2)
print()
print(result_3)
print()

correct_result = time.strftime("%Y/%m/%d %H:%M:%S")
print(correct_result)