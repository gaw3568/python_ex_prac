stringNumber = "4546793"

n_StrNum = list(map(int, stringNumber))
result = []

for idx, num in enumerate(n_StrNum):
    result.append(str(num))
    if idx < len(n_StrNum)-1:
        isOdd = (num % 2 == 1)
        isNextOdd = n_StrNum[idx+1] % 2 == 1
        if isOdd and isNextOdd:
            result.append("-")
        elif not isOdd and not isNextOdd:
            result.append("*")

print("".join(result))