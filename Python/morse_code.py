from variables import MORSE_CODE as code

test_morse = "-.. . -.-. .- -.. . ...-"

def morse(morse_code):
    """
    The Morse code encodes every character as a sequence of "dots" and "dashes".

    For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−.

    The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words.

    For example, the message Decadev in Morse code is -.. . -.-. .- -.. . ...-

    NOTE: Extra spaces before or after the code have no meaning and should be ignored. In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words. Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

    param = morse_code : A string of morse codes
    return word : Converted value of morse code to string
    """ 
    word = []
    if morse_code.find('   '):
        words = morse_code.split('   ')
        for x in words:
            x = x.split(' ')
            initial = ""
            for y in x:
                initial += code[y]
            word.append(initial)
        word = " ".join(word)
                
    else:
        morse_code = morse_code.split(' ') # Breaks codes into array
        for x in morse_code:
            word.append(code[x])
    

    return word


print(morse("-.. . -.-. .- -.. . ...- ..."))

