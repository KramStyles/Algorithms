from string import ascii_lowercase

pos = {}
for idx, item in enumerate(ascii_lowercase):
    pos[item] = str(idx + 1)


def alphabet_position(text):
    """
    In this kata you are required to, given a string,
    replace every letter with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.
    """
    return "".join(
        [f"{pos[item.lower()]} " for item in text if item.lower() in pos]
    ).strip()


print(alphabet_position("The sunset sets at twelve o' clock."))
