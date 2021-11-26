## 문제) 문자열 바꾸기 ##

newString = "a:b:c:d"

# 방법 1
newStr = newString.split(":")
newStr = "#".join(newStr)
print(newStr)

# 방법 2
print(newString.replace(":","#"))