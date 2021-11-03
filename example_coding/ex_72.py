subjects = ["Math", "Korean", "English", "Science", "Society", "Spanish"]

question = str.title(input("Hate subject : "))
if question not in subjects:
    print("There is not your hate subject")
else:
    subjects.remove(question)
print(subjects)