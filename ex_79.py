nums = []

for i in range(3):
    number = int(input("Enter the three numbers : "))
    nums.append(number)
    if i == 2:
        question = input("Do you want to insert last number ? (y/n) ")
        if question == 'n':
            nums.remove(number)

print(nums)