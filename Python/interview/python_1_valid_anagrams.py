import string


def solution(string1, string2):
    """
    Given two strings s1 and s2, check if they are valid anagrams. The two strings
    are anagrams if they are made of the same characters with the same frequencies
    param: string1(str) -≥ input by the user
    param: string2(str) -≥ input by the user
    return (bool) -> True or False

    """
    return sorted(string1) == sorted(string2)

print(solution('danger', 'garden'))
print(solution('hello', 'ellhho'))
print(solution('nameless', 'salesmen'))