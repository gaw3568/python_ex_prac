class FourCal:

    # setdata()와 init() 의 차이는
    # setdata()의 경우, "객체.setdata()" 와 같은 방식으로 객체를 생성하고 객체를 통해 직접 호출해야하지만
    # init의 경우, 생성자이므로 객체 생성 시, 자동으로 호출된다.
    name = "kim chul soo"

    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def setdata(self, num1, num2):
        # cal1.fisrt = num1과 같은 뜻
        self.num1 = num1
        # cal1.second = num2과 같은 뜻
        self.num2 = num2

    def add(self):
        self.result = self.num1 + self.num2
        return self.result
    def sub(self):
        self.result = self.num1 - self.num2
        return self.result
    def mul(self):
        self.result = self.num1 * self.num2
        return self.result
    def div(self):
        self.result = self.num1 / self.num2
        return self.result

class MoreFourCal(FourCal):
    def pow(self):
        self.result = self.num1 ** self.num2
        return self.result

class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

cal1 = SafeFourCal(10,0)

option = int(input("Enter a option : "))
#cal1.setdata(10,4)

if (option == 1):
    result = cal1.add() 
    print(f"{cal1.num1} + {cal1.num2} = {result}")
elif (option == 2):
    result = cal1.sub()
    print(f"{cal1.num1} - {cal1.num2} = {result}")
elif (option == 3):
    result = cal1.mul()
    print(f"{cal1.num1} * {cal1.num2} = {result}")
elif (option == 4):
    result = cal1.div()
    print(f"{cal1.num1} / {cal1.num2} = {result}")
elif (option == 5):
    result = cal1.pow()
    print(f"{cal1.num1}^{cal1.num2} = {result}") 

print(FourCal.name)

# id는 파이썬 내장 함수로, 객체의 주소를 반환하는 함수.
# 주소값을 알아보거나 주소값 비교를 위해서 사용하기 좋음.
# print(id(cal1.num1))
