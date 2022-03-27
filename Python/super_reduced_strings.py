import enum


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
                next = s[index+1]
                if char == next:
                    s.pop(index)
                    s.pop(index)
                    break;
        if s:
            counts = Counter(s).values()
            max_of_each = max(counts)
        else: return 'Empty String'


    return ''.join(s)
    
# superReducedStrings('aaabccddd')
superReducedStrings('aa')