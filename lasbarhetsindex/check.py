#!/usr/bin/env python3
import sys


def count_sentences(text):
    # Räkna antalet meningar i texten
    return text.count('.') + text.count('!') + text.count('?')


def count_words(text):
    # Räkna antalet ord i texten
    return len(text.split())


def count_syllables(word):
    # Räkna antalet stavelser i ett ord
    vowels = "aeiouyåäö"
    num_vowels = 0
    prev_char_is_vowel = False
    for char in word:
        if char.lower() in vowels:
            if not prev_char_is_vowel:
                num_vowels += 1
            prev_char_is_vowel = True
        else:
            prev_char_is_vowel = False
    if word.endswith(('a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö')):
        num_vowels -= 1
    if num_vowels == 0:
        num_vowels = 1
    return num_vowels


def count_syllables_in_text(text):
    # Räkna antalet stavelser i texten
    words = text.split()
    syllables = 0
    for word in words:
        syllables += count_syllables(word)
    return syllables


def calculate_readability_index(text):
    # Beräkna läsbarhetsindexet för texten
    num_sentences = count_sentences(text)
    num_words = count_words(text)
    num_syllables = count_syllables_in_text(text)
    index = (206.835 - (1.015 * (num_words / num_sentences)) - (84.6 * (num_syllables / num_words)) * 1.3)
    return index


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python readability.py filename.txt")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        index = calculate_readability_index(text)
        print(f"The readability index of {filename} is {index:.2f}")
