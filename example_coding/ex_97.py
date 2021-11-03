arr = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]

row, col = map(int, input("Enter row and column : ").split())

if row >= len(arr) or col >= len(arr[0]):
    print("Out of index")
else:    
    print(arr[row][col])