"""Q1:
Write a Python program that takes a sentence from the user and prints:

Number of characters

Number of words

Number of vowels

Hint: Use split(), loops, and vowel checking."""

def analyze_sentence(sentence):
    num_of_char = len(sentence)
    words = sentence.split()
    num_of_words = len(words)
    vowels = 'aeiouAEIOU'
    num_of_vowels = sum(1 for char in sentence if char in vowels)
    return num_of_char, num_of_words, num_of_vowels


user_input = input("Please enter a sentence: ")
char_count, word_count, vowel_count = analyze_sentence(user_input)
print(f"Number of characters: {char_count}")
print(f"Number of words: {word_count}")
print(f"Number of vowels: {vowel_count}")
user_input = input("Please enter a sentence: ")  