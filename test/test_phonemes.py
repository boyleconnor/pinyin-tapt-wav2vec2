import pytest
from generate_data.phonology import chars_to_phonemes


CHINESE_SENTENCES = [
    ("你去过北京吗？", ['n', 'i', '3', 't', 'ɕ', 'ʰ', 'y', '4', 'k', 'w', 'ɔ', '4',
                 'p', 'e', 'ɪ', '3', 't', 'ɕ', 'i', 'ŋ', '1', 'm', 'a', '5',
                 '？']),
    ("我的朋友是Lady Gaga的粉丝", ['w', 'ɔ', '3', 't', 'ɤ', '5', 'p', 'ʰ', 'ɤ', 'ŋ',
                           '2', 'j', 'o', 'ʊ', '3', 'ʂ', 'ɨ', '4',
                           '[NON_CHINESE]', 't', 'ɤ', '5', 'f', 'ə', 'n', '3',
                           's', 'ɯ', '1']),
    ("这里离书店很远。", ['ʈ', 'ʂ', 'ɤ', '4', 'l', 'i', '3', 'l', 'i', '2', 'ʂ',
                  'u', '1', 't', 'j', 'ɛ', 'n', '4', 'x', 'ə', 'n', '3',
                  'ɥ', 'ɛ', 'n', '3', '。']),
    ("他刚才下课了。", ['t', 'ʰ', 'a', '1', 'k', 'ɑ', 'ŋ', '1', 't', 's', 'ʰ', 'a',
                 'ɪ', '2', 'ɕ', 'j', 'a', '4', 'k', 'ʰ', 'ɤ', '4', 'l', 'ɤ',
                 '5', '。'])
]


def test_chars_to_phonemes():
    for chars, expected_pinyin in CHINESE_SENTENCES:
        predicted_chars, predicted_pinyin = chars_to_phonemes(chars)
        assert predicted_pinyin == expected_pinyin
