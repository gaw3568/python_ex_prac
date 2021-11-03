invited_people = []
for i in range(3):
    inviting_people = input("Enter a inviting name : ")
    invited_people.insert(i,inviting_people)

while True:
    add_inviting_people = str.lower(input("Add a inviting name : "))
    if add_inviting_people == 'n' or add_inviting_people == 'no':
        break
    else:
        invited_people.append(add_inviting_people)

print(invited_people)

find_name = input("Enter a name who finds? : ")

print("Index location of entered name :", invited_people.index(find_name))
print("Do you really invite pick name ? ", end="")
answer = str.lower(input("y/n : "))
if answer == 'n' or answer == 'no':
    invited_people.remove(find_name)
    print(invited_people)
else : 
    print("Error")