def top_3_words(text):
    """
        Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

    Assumptions:
    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
    Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
    Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
    """
    from collections import Counter
    from string import punctuation
    import re

    # Splits it to remove most extra chars
    words = [word.lower() for word in text.split()]

    # Checks and removes any symbols inside individual words apart from "'"
    words = [
        word if "'" in word else re.sub(r"[^a-zA-z0-9 ]", "", word) for word in words
    ]

    # Removes ever single quote apart from the ones inside a word
    words = [word for word in words if not re.match(f"^[{punctuation}]+$", word)]

    # Removes any empty value
    words = [word for word in words if word]

    counts = Counter(words).most_common(3)
    print(words)
    return [word[0] for word in counts]
