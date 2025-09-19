line = input("Enter a line of text: ")
words = line.split()
word_count = {word: words.count(word) for word in set(words)}
print("Word occurrences:", word_count)
