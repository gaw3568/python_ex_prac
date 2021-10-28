arr = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]

row = int(input("Enter a row : "))

print(arr[row])

new_value = int(input("Enter a value : "))
arr[row].append(new_value)
print(arr[row])