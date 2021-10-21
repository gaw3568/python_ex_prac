# 원기둥의 부피를 구하는 문제
import math

radius = int(input())
depth = int(input())
area = (radius**2) * math.pi
volume = area * depth

print(round(volume,3))