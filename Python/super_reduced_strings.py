def superReducedStrings(s):
    """
    Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations.
    In each operation, select a pair of adjacent letters that match, and delete them.

    Delete as many characters as possible using this method and return the resulting string.
    If the final string is empty, return Empty String

    Example.

    aab shortens to b in one operation: remove the adjacent a characters.
    Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''.
    Return 'Empty String'.

    Function Description
    Complete the superReducedString function in the editor below.

    aaabccddd → abccddd → abddd → abd

    """
    from collections import Counter

    s = list(s)
    counts = Counter(s).values()
    max_of_each = max(counts)

    while max_of_each > 1:
        for index, char in enumerate(s):
            if index < len(s):
                next = s[index + 1]
                if char == next:
                    s.pop(index)
                    s.pop(index)
                    break
        if s:
            counts = Counter(s).values()
            max_of_each = max(counts)
        else:
            return "Empty String"

    return "".join(s)


def superReducedStrings2(s):
    # from collections import Counter
    # max_of_each = max(Counter(s).values())
    # # while max_of_each > 1:
    group = []
    # for x in s:
    #     if len(group) > 0 and group[-1] == x:
    #         group.pop()
    #     else:
    #         group.append(x)
    groups = [
        group.pop() if len(group) > 0 and group[-1] == x else group.append(x) for x in s
    ]
    if not groups:
        return print("Empty String")
    return print("".join(group))


# superReducedStrings2('aaabccddd')
# superReducedStrings2('aa')
superReducedStrings2("baab")
superReducedStrings2(
    "acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj"
)
