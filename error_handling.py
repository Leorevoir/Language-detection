##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## error_handling
##

import sys

def print_usage():
    print("Welcome to my EPITECH Project !\n")
    print("DESCRIPTION:")
    print("   This is a small HUB project that recognizes language\n")
    print("USAGE:\n   ./language_detection.py <filename>\n")
    print("Copyright (©) Léo QUINZLER Tek1 PGE 2028")
    sys.exit(0)

def parse_arguments(argv):
    if len(argv) < 2:
        print(f"Too few arguments, try {argv[0]} -h for help")
        sys.exit(84)
    if len(argv) > 2:
        print(f"Too many arguments, try {argv[0]} -h for help")
        sys.exit(84)
    if argv[1] == '-h':
        print_usage()
    return argv[1]

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
