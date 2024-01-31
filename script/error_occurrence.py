##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## error_occurrence
##

import sys

def print_usage():
    print("Welcome to my EPITECH Project!\n")
    print("\tDESCRIPTION:")
    print("\tcalculates occurrence letters in a given text")
    print(f"\tUSAGE:\n\t./{sys.argv[1]}  \n")
    print("Copyright (©) Léo QUINZLER Tek1 PGE 2028")
    sys.exit(0)

def try_open(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found.")
        sys.exit(84)

def parse_arguments():
    if len(sys.argv) < 2:
        print(f"Too few arguments, try {sys.argv[0]} -h help\n")
        sys.exit(84)
    if len(sys.argv) > 2:
        print(f"Too many arguments, try {sys.argv[0]} -h help\n")
        sys.exit(84)
    if sys.argv[1] == '-h':
        print_usage()
    return try_open(sys.argv[1])
