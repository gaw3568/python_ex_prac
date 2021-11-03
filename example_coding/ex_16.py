answer = str.lower(input("Is it raining outside? : "))

if answer == 'yes':
    answer_2 = str.lower(input("Is it windy? : "))
    
    if answer_2 == 'yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")        
