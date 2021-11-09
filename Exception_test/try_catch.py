try:
    a = [1,2]
    print(a[2])
    4 / 0
# 1번째 방법
# except:
#    print("Error")

# 2번째 방법
# except ZeroDivisionError:
#    print("Error")


# 3번째 방법    
# except ZeroDivisionError as e:
#    print(e)

# <여러 개의 오류 처리>
# except (IndexError, ZeroDivisionError)와 같은 방식으로도 묶어서 사용할 수 있다. 
except IndexError:
    print("Error2")
except ZeroDivisionError:
    print("Error")

finally:
    print("끝")


try:
    age = int(input("나이를 입력하세요 : "))
except:
    print("입력이 정확하지 않습니다")
else:
    print(f"{age}, 제대로 된 입력입니다")