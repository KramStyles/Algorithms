import imp


def rot13(message):
    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the
    letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13.
    If there are numbers or special characters included in the string, they should be
    returned as they are. Only letters from the latin/english alphabet should be
    shifted, like in the original Rot13 "implementation".
    """
    from string import ascii_lowercase, ascii_uppercase

    result = ""
    for msg in message:
        if msg.isalpha():
            txt_upper = False
            if msg.isupper():
                txt_upper = True
                msg = msg.lower()
            indx = ascii_lowercase.index(msg) + 13
            if indx >= len(ascii_lowercase):
                indx %= len(ascii_lowercase)
            if txt_upper:
                result += ascii_uppercase[indx]
            else:
                result += ascii_lowercase[indx]
        else:
            result += msg
    return result


# rot13('hello')
rot13("NM")
