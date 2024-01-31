##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## error_handling
##

import sys

def print_usage():
    print("Welcome to my EPITECH Project !\n")
    print("\tDESCRIPTION:")
    print("\tThis is a small HUB project that recognizes language")
    print("\tUSAGE:\n\t./language_detection.py <filename>\n")
    print("Copyright (©) Léo QUINZLER Tek1 PGE 2028")
    sys.exit(0)

def parse_arguments():
    if len(sys.argv) < 2:
        print(f"Too few arguments, try {sys.argv[1]} -h help\n")
        sys.exit(0)
    if len(sys.argv) > 2:
        print(f"Too many arguments, try {sys.argv[1]} -h help\n")
        sys.exit(0)
    if sys.argv[1] == '-h':
        print_usage()
    return sys.argv[1]

def try_open(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(84)

def try_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return filename
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(84)
