import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
df_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
phonetic_code_words = [
    f"{letter} for {df_dict.get(letter.upper())}" for letter in user_input]
print(phonetic_code_words)
