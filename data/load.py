from collections import defaultdict, OrderedDict
from typing import TextIO
from tqdm import tqdm
from torchtext.vocab import vocab, Vocab, build_vocab_from_iterator
from data.phonology import chars_to_phonemes, NON_CHINESE_CHAR
from dragonmapper.transcriptions import _IPA_CHARACTERS


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


def get_phoneme_vocab() -> Vocab:
    '''Create a vocabulary for the `phonemes` form of sentences
    '''
    all_ipa = list(_IPA_CHARACTERS.lower())
    all_chars = all_ipa + [NON_CHINESE_CHAR]
    phoneme_vocab = build_vocab_from_iterator(all_chars, specials=[UNK_TOKEN])
    phoneme_vocab.set_default_index(phoneme_vocab[UNK_TOKEN])
    return phoneme_vocab

