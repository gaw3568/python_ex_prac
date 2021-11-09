# 파이썬 내장 클래스 Exception를 상속받아 오류클래스를 만들 수 있다.
class MakeError(Exception):

# 'function annotation' 및 '매개변수:형식'
    # 오류 메시지를 출력했을 때 오류 메시지가 보이게 하기 위해서 오류 클래스에 다음과 같은 __str__ 메서드를 구현
    # -> str : 이 함수가 반환해주는 값의 형식이 String 이라는 것을 말한다.
    def __str__(self) -> str:
        return "잘못된 별명입니다"

# sayNick(매개변수:형식) : 작성된 코드를 볼 때, 변수의 형태를 쉽게 알 수 있게 콜론의 형태로 매개변수의 형태를 지정하게되면 명시적으로 볼 수 있다.
# 주석의 기능을 하기 때문에 코드를 실행하는데 오류를 범하지 않는다.
def sayNick(nickname:str):
    if nickname == "idiot":
        # raise 명령어를 사용해 오류를 강제로 발생시킬 수 있음
        raise MakeError()
    print(nickname)
try:
    sayNick("angel")
    sayNick("idiot")
except MakeError as e:
    print(e)
