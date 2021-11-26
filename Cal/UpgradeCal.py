## Calculator class를 상속하고 minus 기능의 메서드를 가지는 UpgradeCalculator 클래스 생성 문제

from Calculator import *

class UpgradeCalculator(Calculator):
    
    def minus(self,num):
        self.value -= num

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)