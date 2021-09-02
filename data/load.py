from collections import defaultdict
from typing import TextIO
from tqdm import tqdm
from data.phonology import chars_to_phonemes


def load_file(input_file):
    '''Convert every line in input_file into a (characters, phonemes) pair
    '''
    total_lines = len(input_file.readlines())
    input_file.seek(0)

    for line in tqdm(input_file, total=total_lines):
        yield chars_to_phonemes(line)


def generate_vocabularies(input_file: TextIO, min_char_freq: int = 2,
                          min_phoneme_freq: int = 2):
    '''Given an input_file, generate two sets of unique units
    '''
    char_counts, phoneme_counts = defaultdict(int), defaultdict(int)
    for char_sequence, phoneme_sequence in load_file(input_file):
        for char in char_sequence:
            char_counts[char] += 1
        for phoneme in phoneme_sequence:
            phoneme_counts[phoneme] += 1
    char_counts, phoneme_counts = dict(char_counts), dict(phoneme_counts)

    chars = sorted(filter(lambda c: char_counts[c] >= min_char_freq,
                          char_counts.keys()))
    phonemes = sorted(filter(lambda p: phoneme_counts[p] >= min_phoneme_freq,
                             phoneme_counts.keys()))

    return chars, phonemes
