import pytest
from generate_data.pinyin import to_pinyin


CHINESE_SENTENCES = [
    ("你去过北京吗？", ['ni3', 'qu4', 'guo4', 'bei3', 'jing1', 'ma5', '？']),
    ("我的朋友是Lady Gaga的粉丝", ['wo3', 'de5', 'peng2', 'you3', 'shi4',
                           '[NON_CHINESE]', 'de5', 'fen3', 'si1']),
    ("这里离书店很远。", ['zhe4', 'li3', 'li2', 'shu1', 'dian4', 'hen3', 'yuan3', '。']),
    ("他刚才下课了。", ['ta1', 'gang1', 'cai2', 'xia4', 'ke4', 'le5', '。'])
]


def test_chars_to_pinyin():
    for chars, expected_pinyin in CHINESE_SENTENCES:
        predicted_chars, predicted_pinyin = to_pinyin(chars)
        assert predicted_pinyin == expected_pinyin
