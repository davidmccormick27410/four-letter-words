"""
This script extracts four letter words from a dictionary of words used in Scrabble.
"""
from pathlib import Path
import pandas as pd

file_path = Path('data\\dictionary.txt')

col_names = ['word']
df = pd.read_csv(file_path, header=None, names=col_names)

exact_df = df[df['word'].str.len() == 4]

exact_df.to_csv('data\\four_letter_words.csv')
