class RomanNumerals:
    """
    Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
    It should follow the API demonstrated in the examples below. Multiple roman numeral values will 
    be tested for each helper method.

    Modern Roman numerals are written by expressing each digit separately starting with the left 
    most digit and skipping any digit with a value of zero. 
    In Roman numerals 1990 is rendered: 
    1000=M, 900=CM, 90=XC; resulting in MCMXC. 

    2008 is written as 2000=MM, 8=VIII; or MMVIII. 

    1666 uses each Roman symbol in descending order: MDCLXVI.

    Input range : 1 <= n < 4000
    In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
    """

    romans = {
        'I':	1,
        'IV':	4,
        'V':	5,
        'X':	10,
        'L':	50,
        'C':	100,
        'D':	500,
        'M':	1000,
    }
    romans_values = list(romans.values())

    def to_roman(val):
        numbers = []
        RN = ''
        for idx, num in enumerate(str(val)):
            zeros = '0'* (len(str(val)) - idx-1)
            numbers.append(num+zeros)

        print(numbers)
        
        for num in numbers:
            highest = max([high for high in RomanNumerals.romans_values if high <= int(num)])
            print(highest, int(num) / highest)

    def from_roman(roman_num):
        print('hello')

RomanNumerals.to_roman(2469)