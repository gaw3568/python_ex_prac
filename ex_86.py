pswd = input("Enter a password : ")
re_pswd = input("Enter a password again : ")

if pswd == re_pswd:
    print("Thank you")
elif pswd.lower() == re_pswd.lower():
    print("They must be in the same case")
elif pswd != re_pswd:
    print("Incorrect")