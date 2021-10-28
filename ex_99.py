arr = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]

row = int(input("Enter a row : "))
print(arr[row])

col = int(input("Enter a column : "))
print(arr[row][col])

answer = input("Do you want to change " + str(arr[row][col]) + " ? (y/n) ")

if answer == 'y' or answer == 'yes':
    new_value = int(input("Enter a new value : "))
    arr[row][col] = new_value

print(arr[row])