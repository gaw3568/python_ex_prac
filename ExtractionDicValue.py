## 문제) 딕셔너리 값 추출하기 ##

a = {'A':90, 'B':80}
try:
    print(a['C'])
except KeyError :
    print(70)