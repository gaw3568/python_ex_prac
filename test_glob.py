## glob 모듈을 사용해 원하는 디렉터리 안에 존재하는 python파일만 모두 출력하는 예제
import glob

result = glob.glob("/Users/jewon/Desktop/python_ex_prac/*.py")
for x in result:
    print(x)
