#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## language
## File description:
## language_detection
##

from csv_handling import *
from error_handling import *

def detect_language(text, letter_frequencies, languages):
    text = text.lower()
    text_frequencies = count_letter_frequencies(text)    
    best_language = ""
    best_score = float('inf')

    for language in languages:
        score = calculate_score(text_frequencies, letter_frequencies, language)

        if score < best_score:
            best_score = score
            best_language = language

    return best_language

def count_letter_frequencies(text):
    text_frequencies = {}

    for letter in text:

        if letter.isalpha():

            if letter in text_frequencies:
                text_frequencies[letter] += 1
            else:
                text_frequencies[letter] = 1

    return text_frequencies

def calculate_score(text_frequencies, letter_frequencies, language):
    score = 0
    total_freq = sum(text_frequencies.values())

    for letter, freq in text_frequencies.items():

        if letter in letter_frequencies and language in letter_frequencies[letter]:
            expected_freq = letter_frequencies[letter][language]
            score += abs(freq / total_freq * 100 - expected_freq)
        else:
            score += freq if letter in text_frequencies else 0

    return score

def main():
    file_path = parse_arguments(sys.argv)

    text = try_open(file_path)
    latine_file = try_csv("data/occurrence/latine.csv")
    cyrillic_file = try_csv("data/occurrence/cyrillic.csv")

    letter_frequencies, languages = load_csv(latine_file, cyrillic_file)
    detected_language = detect_language(text, letter_frequencies, languages)

    print(f"Detected language: {detected_language}")

if __name__ == "__main__":
    main()
