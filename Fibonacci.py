def Fibo(num):
    if num < 2:
        return num
    else:
        return Fibo(num - 2) + Fibo(num - 1)

number = int(input("Enter a number : "))

for num in range(number):
    print(Fibo(num))
