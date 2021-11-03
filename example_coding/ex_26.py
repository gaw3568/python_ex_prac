word = input("Enter word : ")
first_word = word[0].lower()
if first_word == 'a' or first_word == 'e' or first_word == 'i' or first_word == 'o' or first_word == 'u':
    word = word + "way"
    print(word.lower())
else:
    word = word[1:len(word)] + word[0] + "ay"
    print(word.lower())
