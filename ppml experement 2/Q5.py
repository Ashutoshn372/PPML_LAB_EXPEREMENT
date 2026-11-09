# Question 5: Enter a string, print it in reverse, and count its vowels and consonants.

text = input("Enter a string: ")
vowel_count = 0
consonant_count = 0

for character in text:
    if character.isalpha():
        if character.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

print("Reversed string:", text[::-1])
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)