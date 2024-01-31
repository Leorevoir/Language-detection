##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## what_letters
##
#ne calcule que l'alphabet majoritaire
#par exemple si dans un texte français il y a du cyrillic,
#il ne calculera que l'occurrence des lettres latines

import re

def is_latine(letter):
    return re.match(r'[a-zA-Z]', letter)

def is_cyrillic(letter):
    return re.match(r'[а-яА-Я]', letter)

def cyrillic_letters(text):
    return len([letter for letter in text if is_cyrillic(letter)])

def latin_letters(text):
    return len([letter for letter in text if is_latine(letter)])
