# Pangrams
import string


def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False
    return True


sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")
