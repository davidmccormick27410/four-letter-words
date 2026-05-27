"""
This script extracts four letter words from a dictionary of words used in Scrabble.
"""
from pathlib import Path

file_path = Path('data\\dictionary.txt')

with open(file_path, "r", encoding="utf-8") as file_object:
    # Perform file operations here
    the_file = file_object.read().splitlines()

four_letter_words = [x for x in the_file if len(x) == 4]


# 'w' mode overwrites existing content. Use 'a' to append.
with open("data\\four_letter_words.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(four_letter_words) + "\n")



