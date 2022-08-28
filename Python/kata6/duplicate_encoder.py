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
    

    # return ''.join([if item in existing '(' else ')' for item in word])
    # return ''.join('(' if item in existing else existing.append(item) & ')' for item in word)
    # existing = []
    # new_word = ''
    # for item in word:
    #     if item in existing:
    #         new_word += ')'
    #     else:
    #         existing.append(item)
    #         new_word += '('
    # return new_word

    from collections import Counter
    
    words = Counter(word.lower())

    return ''.join(['(' if words[item] == 1 else ')' for item in word.lower()])

print(duplicate_encode('din'))
print(duplicate_encode('recede'))
print(duplicate_encode('Success'))
print(duplicate_encode('(( @'))


