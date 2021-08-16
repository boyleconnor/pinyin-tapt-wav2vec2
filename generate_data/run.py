import re
import zhon.hanzi
from g2pM import G2pM


NON_CHINESE_CHAR = '[NON_CHINESE]'
CHINESE_PATTERN = \
    '[{}{}]'.format(zhon.hanzi.characters, zhon.hanzi.punctuation)


g2pm = G2pM()


def to_pinyin(line: str) -> (list[str], list[str]):
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
        else:
            non_chinese.append(character)

    # Convert output characters to pinyin
    # TODO: Should we split into phonetic parts at this point?

    output_pinyin = [] if len(output_chars) == 0 else g2pm(output_chars)

    return output_chars, output_pinyin


def run():
    """Download common crawl if not already downloaded, then convert to pinyin

    generate pinyinized file thereof.
    :return:
    """
    # TODO: implement download section

    with open('generate_data/example_chinese.txt') as data_file:
        for line in data_file:
            chars, pinyin = to_pinyin(line)
            print(f"original:\n{line}")
            print(f"pre-proc'd chars:\n{chars}")
            print(f"pinyin:\n{pinyin}")
            print("")


if __name__ == '__main__':
    run()
