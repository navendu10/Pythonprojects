text = "I like to like a game"
word = "like"

words = text.split(" ")
count = text.count(word)

frequency = count / len(words) * 100
print(frequency)