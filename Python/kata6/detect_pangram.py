def is_pangram(sentence):
    """
    A pangram is a sentence that contains every single letter of the alphabet 
    at least once. For example, the sentence "The quick brown fox jumps over 
    the lazy dog" is a pangram, because it uses the letters A-Z at 
    least once (case is irrelevant).

    Given a string, detect whether or not it is a pangram. Return True if it 
    is, False if not. Ignore numbers and punctuation.
    """
    # Import lowercase characters
    from string import ascii_lowercase

    # Convert sentence to lowercase
    sentence = sentence.lower()
    
    # loop through alphabets and end loop if it doesn't exist
    for char in ascii_lowercase:
        if char not in sentence:
            return False

    return True

sentence1 = "The quick, brown fox jumps over the lazy dog!"
sentence2 = "1bcdefghijklmnopqrstuvwxyz"
print(is_pangram(sentence1))
print(is_pangram(sentence2))