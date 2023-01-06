def fake_bin(x):
    """
    Given a string of digits, you should replace any digit below 5 with '0'
    and any digit 5 and above with '1'. Return the resulting string.

    Note: input will never be an empty string
    """
    return "".join(["0" if int(dig) < 5 else "1" for dig in x])
