file = open("abc.txt", "r")
lines = file.readlines()
file.close()

lines.reverse()

with open("abc.txt", "w") as file:
    for line in lines:
        line = line.strip()
        file.write(line)
        file.write("\n")
