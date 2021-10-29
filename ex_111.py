file_csv = open("Books.csv","w")

line = "To Kill A Mockingbird, Harper Lee, 1960\n"
file_csv.write(line)
line = "A Brief History Of Time, Stephen Hawking, 1988\n"
file_csv.write(line)
line = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file_csv.write(line)
line = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file_csv.write(line)
line = "Pride and Prejudice, Jane Austen, 1813\n"
file_csv.write(line)

file_csv.close()
