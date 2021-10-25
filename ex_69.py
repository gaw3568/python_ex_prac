nations = ("France","Republic of korea","Germany","United of kingdom","Espanol")
print(nations)

answer = str.title(input("Enter a nation : "))
if answer not in nations:
    print("Error")
else :
    print(nations.index(answer))