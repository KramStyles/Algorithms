def duplicate_count(text):
    """Write a function that will return the count of distinct case-insensitive
    alphabetic characters and numeric digits that occur more than once in
    the input string. The input string can be assumed to contain only
    alphabets (both uppercase and lowercase) and numeric digits."""

    from collections import Counter

    dups = Counter(text.lower())
    counter = 0
    for dup in dups.items():
        if dup[1] > 1:
            counter += 1

    print(counter)


duplicate_count("Indivisibilitiessssssssssssss")
