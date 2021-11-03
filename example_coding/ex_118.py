def save_number():
    num = int(input("Enter a number : "))
    return num

def counting(number):
    for i in range(1,number + 1):
        count = i
        print(count)    

def main():
    number = save_number()
    counting(number)

main()