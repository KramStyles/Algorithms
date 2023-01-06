def gibonacci(n, x, y):
    number = n
    first = x
    second = y

    if number == 0:
        return first
    if number == 1:
        return second

    for i in range(2, number + 1):
        current = second - first
        first = second
        second = current
    return current


print(gibonacci(3, 0, 1))  # should print 0
