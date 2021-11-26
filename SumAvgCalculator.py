class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList
    
    def sum(self):
        totalSum = 0
        for num in self.numberList:
            totalSum += num
        return totalSum

    def avg(self):
        total = self.sum()
        return total / len(self.numberList)

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

cal1 = Calculator(list_1)
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator(list_2)
print(cal2.sum())
print(cal2.avg())