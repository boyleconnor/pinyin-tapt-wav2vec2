from collections import defaultdict, OrderedDict
from typing import TextIO
from tqdm import tqdm
from torchtext.vocab import vocab, Vocab
from data.phonology import chars_to_phonemes


UNK_TOKEN = '<UNK>'


def load_file(input_file):
    '''Convert every line in input_file into a (characters, phonemes) pair
    '''
    total_lines = len(input_file.readlines())
    input_file.seek(0)

    for line in tqdm(input_file, total=total_lines):
        yield chars_to_phonemes(line)


def generate_char_vocab(input_file: TextIO, min_freq: int = 2) -> Vocab:
    '''Given an input_file, generate two sets of unique units
    '''
    char_counts, _ = defaultdict(int), defaultdict(int)
    for char_sequence, phoneme_sequence in load_file(input_file):
        for char in char_sequence:
            char_counts[char] += 1

    # Create character vocab, with OOV token
    char_counts = OrderedDict(
        sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
    char_vocab = vocab(char_counts, min_freq=min_freq)
    char_vocab.insert_token(UNK_TOKEN, 0)
    char_vocab.set_default_index(char_vocab[UNK_TOKEN])

    return char_vocab
