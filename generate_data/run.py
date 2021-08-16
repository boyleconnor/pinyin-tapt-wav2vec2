from g2pM import G2pM


NON_CHINESE_CHAR = '[NON_CHINESE]'
# FIXME: Install real constants for the following two:
CHINESE_CHARS = {'下', '丝', '书', '了', '京', '他', '你', '刚', '北', '去', '友',
                 '吗', '店', '很', '我', '才', '是', '朋', '的', '离', '粉', '课',
                 '过', '这', '远', '里'}
CHINESE_PUNCS = {'。', '？'}


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
        if character in (CHINESE_CHARS | CHINESE_PUNCS) \
                and len(non_chinese) == 0:
            output_chars.append(character)
        elif character in (CHINESE_CHARS | CHINESE_PUNCS):
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
