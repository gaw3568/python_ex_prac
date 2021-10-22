answer = str.upper(input("count UP or DOWN ? "))

if answer == 'UP':
    number = int(input("Enter the Biggest numer : "))
    
    for i in range(1,number+1):
        print(i)
elif answer == 'DOWN':
    number = int(input("Enter a number between 1 and 20 : "))
    for i in range(20,number-1,-1):
        print(i)
else:
    print("I don't understand")
