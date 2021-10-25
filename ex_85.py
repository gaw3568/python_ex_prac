name = str.lower(input("Enter your name : "))

count = 0

for x in name:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        count += 1
print(count)
