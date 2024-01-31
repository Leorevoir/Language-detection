#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## occurrence_generator
##

from what_letters import *
from error_occurrence import *

def calculate_letter_frequencies(text):
    text = text.lower()
    total_letters = len(text)
    letter_frequencies = {}

    if cyrillic_letters(text) > latin_letters(text):
        letter_frequencies = calculate_frequencies(text, is_cyrillic)
    else:
        letter_frequencies = calculate_frequencies(text, is_latine)

    for letter, frequency in letter_frequencies.items():
        percentage = (frequency / total_letters) * 100
        print(f"{letter}: {percentage:.4f}")

def calculate_frequencies(text, is_letter_type):
    letter_frequencies = {}
    for letter in text:
        if is_letter_type(letter):
            if letter in letter_frequencies:
                letter_frequencies[letter] += 1
            else:
                letter_frequencies[letter] = 1
    return letter_frequencies

def main():
    text = parse_arguments()
    calculate_letter_frequencies(text)

if __name__ == "__main__":
    main()
