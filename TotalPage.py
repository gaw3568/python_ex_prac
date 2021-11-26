
def getTotalPage(m,n) -> int:
    if m % n == 0:
        result = m // n
    else:
        result = (m // n) + 1
    return result

## m: 게시물의 총 건수 / n: 한 페이지에 보여줄 수 있는 게시물의 수
m, n = map(int,(input("m, n : ").split()))

print(f"Total Page : {getTotalPage(m,n)}")