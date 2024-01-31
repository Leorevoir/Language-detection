
##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## unit_test
##

import unittest
import sys
import os
import tempfile

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
sys.path.append(os.path.join(parent_dir, 'data'))

from language import *
from test_text import *

class TestLanguageDetection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        latine_file = try_csv("data/occurrence/latine.csv")
        cyrillic_file = try_csv("data/occurrence/cyrillic.csv")
        cls.letter_frequencies, cls.languages = load_csv(latine_file, cyrillic_file)
    
    def setUp(self):
        self.latine_file = tempfile.NamedTemporaryFile(delete=False)
        self.cyrillic_file = tempfile.NamedTemporaryFile(delete=False)

        with open(self.latine_file.name, 'w') as f:
            f.write("Letter;English;French;German\n")
            f.write("a;10;15;20\n")

        with open(self.cyrillic_file.name, 'w') as f:
            f.write("Letter;Russian;Ukrainian\n")
            f.write("б;5;8\n")

    def test_english(self):
        self.assertEqual(detect_language(english_text, self.letter_frequencies, self.languages), 'English')

    def test_french(self):
        self.assertEqual(detect_language(french_text, self.letter_frequencies, self.languages), 'French')

    def test_german(self):
        self.assertEqual(detect_language(german_text, self.letter_frequencies, self.languages), 'German')

    def test_spanish(self):
        self.assertEqual(detect_language(spanish_text, self.letter_frequencies, self.languages), 'Spanish')

    def test_italian(self):
        self.assertEqual(detect_language(italian_text, self.letter_frequencies, self.languages), 'Italian')

    def test_turkish(self):
        self.assertEqual(detect_language(turkish_text, self.letter_frequencies, self.languages), 'Turkish')

    def test_swedish(self):
        self.assertEqual(detect_language(swedish_text, self.letter_frequencies, self.languages), 'Swedish')

    def test_polish(self):
        self.assertEqual(detect_language(polish_text, self.letter_frequencies, self.languages), 'Polish')

    def test_dutch(self):
        self.assertEqual(detect_language(dutch_text, self.letter_frequencies, self.languages), 'Dutch')

    def test_portuguese(self):
        self.assertEqual(detect_language(portuguese_text, self.letter_frequencies, self.languages), 'Portuguese')

    def test_danish(self):
        self.assertEqual(detect_language(danish_text, self.letter_frequencies, self.languages), 'Danish')

    def test_icelandic(self):
        self.assertEqual(detect_language(icelandic_text, self.letter_frequencies, self.languages), 'Icelandic')

    def test_finnish(self):
        self.assertEqual(detect_language(finnish_text, self.letter_frequencies, self.languages), 'Finnish')

    def test_russian(self):
        self.assertEqual(detect_language(russian_text, self.letter_frequencies, self.languages), 'Russian')

    def test_ukrainian(self):
        self.assertEqual(detect_language(ukrainian_text, self.letter_frequencies, self.languages), 'Ukrainian')

if __name__ == '__main__':
    unittest.main()
