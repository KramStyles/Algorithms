def move_zeros(array):
    """
    Write an algorithm that takes an array
    and moves all of the zeros to the end,
    preserving the order of the other elements.
    Took me from 191 to 244. Kata 5

    First algorithm i wrote and it passed all test at once. Wonderful
    """
    zeros = array.count(0)
    if zeros:
        while zeros > 0:
            for idx, dig in enumerate(array):
                if dig == 0:
                    array.remove(dig)
                    array.insert(len(array), dig)
                    zeros -= 1
                    break
    return array


def move_zeros_shor(array):
    return [x for x in array if x] + [0] * array.count(0)


move_zeros([1, 0, 1, 2, 0, 1, 3])
