class Human:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def info(self):
        print(f"나의 이름은 {self.name}, 나이는 {self.age}살 입니다")

human1 = Human("짱구", "10")
human2 = Human("철수", "12")
human1.info()
human2.info()

human3 = Human("유리", "13")
human4 = Human("훈이", "11")
human3.info()
human4.info()