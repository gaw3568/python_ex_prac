bottle = 10

while bottle > 0:
    print("There are ",bottle,"green bottles hanging on the wall,",bottle,"green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    print("how many green bottles will be hanging on the wall?")
    bottle -= 1
    number = int(input("Enter a number : "))
    
    if number == bottle:
        print("There will be",bottle,"green bottles hanging on the wall")
    else:
        print("No, try again")

print("There are no more green bottles hanging on the wall")

