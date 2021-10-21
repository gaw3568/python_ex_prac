name = input("enter your name : ")

if len(name) < 5:
    last_name = input()
    name = name + last_name
    print(name.upper())
elif len(name) >= 5:
    print(name.lower())