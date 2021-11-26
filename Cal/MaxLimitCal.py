from Calculator import *

class MaxLimitCalculator(Calculator):
    def add(self, num:int) -> None:
        self.value += num
        if (self.value >= 100):
            print("Number is over than 100")
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

