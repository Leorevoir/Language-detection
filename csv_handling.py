##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## csv_handling
##

import csv

def read_csv(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        return list(reader)

def update_frequencies(letter_frequencies, languages, letter, language, freq):
    if freq != '':
        if letter not in letter_frequencies:
            letter_frequencies[letter] = {}

        letter_frequencies[letter][language] = float(freq)
        languages.add(language)

def process_csv_data(reader):
    letter_frequencies = {}
    languages = set()

    for row in reader:
        letter = row['Letter']

        for language in reader[0].keys():
            if language != 'Letter':
                freq = row[language]
                update_frequencies(letter_frequencies, languages, letter, language, freq)

    return letter_frequencies, languages

def merge_frequencies(freq_1, freq_2):
    for letter, languages in freq_2.items():

        if letter not in freq_1:
            freq_1[letter] = languages
        else:
            for language, freq in languages.items():
                freq_1[letter][language] = freq

    return freq_1

def load_csv_file(csv_file):
    reader = read_csv(csv_file)
    return process_csv_data(reader)

def load_csv(latine_file, cyrillic_file):
    freq_1, latine_languages = load_csv_file(latine_file)
    freq_2, cyrillic_languages = load_csv_file(cyrillic_file)

    merged_frequencies = merge_frequencies(freq_1, freq_2)
    merged_languages = latine_languages.union(cyrillic_languages)

    return merged_frequencies, list(merged_languages)