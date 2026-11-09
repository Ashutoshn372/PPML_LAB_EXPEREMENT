# Question 5: Print the even-length words in a string.

text = input("Enter a string: ")
even_length_words = [word for word in text.split() if len(word) % 2 == 0]

if even_length_words:
    print("Even-length words:", " ".join(even_length_words))
else:
    print("There are no even-length words.")