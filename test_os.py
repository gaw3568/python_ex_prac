## os 모듈을 사용하여 위치해있는 디렉터리의 파일목록을 출력하는 예제
import os

os.chdir("/Users/jewon/Desktop/python_ex_prac")
result = os.popen("ls")
print(result.read())