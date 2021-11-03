message = input("Enter your message : ")

while True:
    if message.islower() or message.istitle():
        print("Enter your message to uppercase again")
        message = input("Enter your message : ")
    else:
        print("Exact Message case")
        break    