def convert(numbers):
    numbers = "0" + str(numbers).replace(" ", "")[-10:]
    return numbers if len(numbers) == 11 else "Invalid Input"


print(convert("+234 706 518 6939"))
print(convert("+2347065186939"))
print(convert(2347065186939))


import re


def mating(number, alphabets):
    proof = re.findall(r"B8|8B", alphabets)
    conclusion = len(proof) >= number
    return ["".join(proof), conclusion]


print(mating(3, "b3b3B8B8B8b8b3b3b3b8Bb3b3b3"))
