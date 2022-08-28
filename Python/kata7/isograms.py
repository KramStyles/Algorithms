def isograms(string):
    """
    An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    Implement a function that determines whether a string that contains only letters
    is an isogram. Assume the empty string is an isogram. 
    """
    res = []
    for letter in string:
        if res and letter.lower() in res:
            return False
        else: res.append(letter)
    return True

    # Shorter solution
    #  return len(string) == len(set(string.lower()))

isograms('Dermatoglyphics')
isograms('moose4you')
isograms('abA')