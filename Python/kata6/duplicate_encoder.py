def duplicate_encode(word):
    """
        The goal of this exercise is to convert a string to a new string where each character 
        in the new string is "(" if that character appears only once in the 
        original string, or ")" if that character appears more than once in the 
        original string. Ignore capitalization when determining if a character
        is a duplicate.

        Examples
        "din"      =>  "((("
        "recede"   =>  "()()()"
        "Success"  =>  ")())())"
        "(( @"     =>  "))((" 
    """
    existing = []
    # return ''.join([if item in existing '(' else ')' for item in word])
    # return ''.join('(' if item in existing else existing.append(item) & ')' for item in word)
    new_word = ''
    for item in word:
        if item in existing:
            new_word += ')'
        else:
            existing.append(item)
            new_word += '('
    return new_word

print(duplicate_encode('recede'))


