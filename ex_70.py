nations = ("France","Republic of korea","Germany","United of kingdom","Espanol")

number = int(input("Enter a number : "))

if number >= len(nations):
    print("Your number is too big")    
else :
    print(nations[number])