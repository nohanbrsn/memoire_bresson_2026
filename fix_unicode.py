#!/usr/bin/env python3
import unicodedata
import sys

# Read the file
with open('Template_Mémoire__Copy_/main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize to NFC (composed form)
normalized_content = unicodedata.normalize('NFC', content)

# Write back
with open('Template_Mémoire__Copy_/main.tex', 'w', encoding='utf-8') as f:
    f.write(normalized_content)

print("✓ File normalized to NFC form (composed Unicode characters)")
