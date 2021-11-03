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

print("Adding people :",invited_people[3:], ", Total adding people : " + str(len(invited_people)))
