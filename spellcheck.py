# Spelling Checker
# pip install pyspellchecker
from spellchecker import SpellChecker
def spell_check_word(word):
    # Create a SpellChecker instance
    speller = SpellChecker()
    # Generate suggestions for the misspelled word
    corrections = speller.candidates(word)
    print("Correction: ", corrections)
spell_check_word('mussage')