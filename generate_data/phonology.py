import re
from typing import List
import zhon.hanzi
from dragonmapper.transcriptions import pinyin_to_ipa
from g2pM import G2pM


NON_CHINESE_CHAR = '[NON_CHINESE]'
CHINESE_PATTERN = \
    '[{}{}]'.format(zhon.hanzi.characters, zhon.hanzi.punctuation)


g2pm = G2pM()


def pinyin_to_phonemes(syllable: str) -> str:
    """Convert syllable of pinyin to phonemes (e.g. 'qu4' -> 'tɕʰy4')
    """
    # Extract tone (keep as number)
    tone = syllable[-1]

    # These special cases make up for a bug in dragonmapper, which should be
    # addressed in PR #31.
    if syllable[:-1] == 'yong':
        phonemes = 'jʊŋ'
    elif syllable[:-1] == 'you':
        phonemes = 'joʊ'
    elif syllable[:-1] == 'o':
        phonemes = 'ɔ'
    elif syllable[:-1] == 'yo':
        phonemes = 'jɔ'
    else:
        # The .replace() fixes a point of disagreement
        phonemes = pinyin_to_ipa(syllable[:-1]).replace('œ', 'ɛ')
    return phonemes + tone


def chars_to_phonemes(line: str) -> (List[str], List[str]):
    """Convert single line of Chinese characters (incl. other writing systems)
    to tokenized sequences of Chinese characters and pinyin.

    e.g. "他现在在Berlin。" -> (["他", "现", "在", "在", "[NON_CHINESE]", "。"],
        ["ta1", "xian4", "zai4", "zai4", "[NON_CHINESE]"])

    :param line:
    :return (characters, pinyin):
    """
    output_chars = []
    non_chinese = []

    # Create pre-processed output characters
    for character in line:
        if re.match(CHINESE_PATTERN, character) and len(non_chinese) == 0:
            output_chars.append(character)
        elif re.match(CHINESE_PATTERN, character):
            # De-queue the stored non-Chinese text section
            output_chars.append(NON_CHINESE_CHAR)
            non_chinese = []
            output_chars.append(character)
        else:
            non_chinese.append(character)
    if len(non_chinese) > 0:
        output_chars.append(NON_CHINESE_CHAR)

    # Convert output characters to pinyin
    output_pinyin = [] if len(output_chars) == 0 else g2pm(output_chars)

    # Convert pinyin to phonemes
    output_phonemes = []
    for syllable in output_pinyin:
        if syllable != NON_CHINESE_CHAR and not \
                re.match(CHINESE_PATTERN, syllable):
            phonemes = pinyin_to_phonemes(syllable.replace('u:', 'ü'))
            output_phonemes.extend(phonemes)
        else:
            output_phonemes.append(syllable)

    return output_chars, output_phonemes
