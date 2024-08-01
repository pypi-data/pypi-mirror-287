import re 
import requests 
from bs4 import BeautifulSoup

def normalize_text(text):
    replacements = {
        '–': '-',  # en dash
        '—': '-',  # em dash
        '’': '\'',  # right single quotation mark to straight apostrophe
        # add more replacements as needed
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def is_valid_cell(cell):
    # Check each character in the cell
    allowed = ['-', '/', ':', ',', '.', ' ', '(', ')', '’']
    normal_cell = normalize_text(cell)
    for char in normal_cell:
        stripped_char = char.strip()
        for value in allowed:
            if not stripped_char.isascii() and stripped_char != value:
                print(f"Invalid character found: '{stripped_char}' (Unicode: {ord(stripped_char)})")
                return False
    return True
