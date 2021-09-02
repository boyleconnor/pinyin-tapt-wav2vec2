import argparse
import json
from data.load import generate_vocabularies


def run(input_file, min_char_freq, min_phoneme_freq, output_file):
    chars, phonemes = generate_vocabularies(input_file, min_char_freq,
                                            min_phoneme_freq)
    vocabs = {'chars': chars, 'phonemes': phonemes}
    json.dump(vocabs, output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print original and '
                                                 'preprocessed content from '
                                                 'first n lines of file')
    parser.add_argument('input_file', type=argparse.FileType('r'))
    parser.add_argument('output_file', type=argparse.FileType('w'))
    parser.add_argument('--min-char-freq', type=int, default=2)
    parser.add_argument('--min-phoneme-freq', type=int, default=2)
    args = parser.parse_args()

    run(args.input_file, args.min_char_freq, args.min_phoneme_freq,
        args.output_file)
