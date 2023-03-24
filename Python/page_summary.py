def pages(summary):
    hold = counter = 0
    for num in range(1, summary + 1):
        if hold >= summary:
            return print(counter)
        hold += len(str(num))
        counter += 1
    return print(counter)


def pages_shorter(summary):
    """
    Every book has n amount of pages. You will be given the summary which was made by adding
    up the number of digits contained in each page number in a book(from 1 to n).
    The task is to find how many pages a book has- n.

    Example
    When input is 25 (summary). The output must be 17(n).
    There are 9 one-digit pages and 8 two-digit pages(8 ones and 8 digits from 0 to 7)

    Be aware that you'll get enormous books having up to 100.000 pages.

    All input will be valid
    """
    pagecount = 0
    i = 0
    while summary != pagecount:
        i += 1
        pagecount += len(str(i))
    return i


pages_shorter(25)
pages_shorter(5)
pages(185)
pages(1095)
pages(660)
