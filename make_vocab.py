import argparse
import torch
from data.load import generate_char_vocab


def run(input_file, min_char_freq, output_file):
    char_vocab = generate_char_vocab(input_file, min_char_freq)
    torch.save(char_vocab, output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print original and '
                                                 'preprocessed content from '
                                                 'first n lines of file')
    parser.add_argument('input_file', type=argparse.FileType('r'))
    parser.add_argument('output_file', type=argparse.FileType('wb'))
    parser.add_argument('--min-char-freq', type=int, default=2)
    args = parser.parse_args()

    run(args.input_file, args.min_char_freq, args.output_file)
