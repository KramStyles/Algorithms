array = [1, 2, 3, 4]
seq1 = [2, 4]
seq2 = [1, 3, 4]

array2 = [5, 1, 22, 25, 6, -1, 8, 10]
seq3 = [1, 6, -1, 10, 11]


def validate_sequence(array, sequence):
    test = []  # To hold our index
    valid = True  # To validate our sequence
    for x in sequence:  # To find the index of numbers in the array
        if x in array2:  # Make sure the number in the sequence exists
            test.append(array.index(x))  # appends index to test

    for x, y in enumerate(test):  #
        if x > 0:
            if y < test[x - 1]:
                valid = False

    return valid


print(validate_sequence(array2, seq3))
