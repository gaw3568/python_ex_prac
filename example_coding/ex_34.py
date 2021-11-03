print("1) Square")
print("2) Triangle\n")
print("Enter a number:")

input_number = int(input())
if input_number == 1:
    length = int(input())
    area = length * length
    print("넓이:",area)
elif input_number == 2:
    bottom = int(input())
    height = int(input())
    triangle_area = (bottom * height) / 2
    print("넓이:", triangle_area)
else:
    print("Error")    