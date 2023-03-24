def counts(arr):
    """
    Return an array, where the first element is the count of positives numbers
    and the second element is sum of negative numbers. 0 is neither positive nor negative.

    If the input is an empty array or is null, return an empty array.
    """
    res = []
    if not arr:
        return res
    res = [0, 0]
    for num in arr:
        if num > 0:
            res[0] += 1
        elif num < 0:
            res[1] += num

    return res
