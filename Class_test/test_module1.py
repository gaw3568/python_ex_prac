# "from 모듈이름 import 모듈함수" 의 형태로도 사용가능
#  모든 함수를 사용하고 싶은 경우 import 뒤에 "*" 를 붙이면 된다.
# from module1 import *
# from module1 import add
import module1

num1 = 3
num2 = 6

print(module1.__name__)
print(module1.add(num1, num2))
print(module1.sub(num1, num2))
