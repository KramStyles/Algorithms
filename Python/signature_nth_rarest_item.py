"""
Given a list of integers, create a function that returns the nth-rarest item. 
The function should be called nth_most_rare signature and its signarture nth_most_rate signature (list, n)
where list is the array of integers and n is the nth rarest term. 

For example in ([5,4,5,4,5,4,4,5,3,3,3,2,2,1,5]), if 2 is supplied as n, the answer is 2 as 2 is the 2nd rarest item
"""


def nth_most_rate(array: list, n: int):
    """
    This function goes through the list and finds the nth rarest item (n).
    This would be implemented with the builtin collections.Counter method in python
    params
    array: (list) => List of integers
    n: (int) => Nth rare item
    return result: (int) Nth rarest item from the array
    """

    from collections import Counter
    items = Counter(array)

    return items[n]


def nth_most_rate2():
    """
    This function goes through the list and finds the nth rarest item (n)
    params
    array: (list) => List of integers
    n: (int) => Nth rare item
    return result: (int) Nth rarest item from the array
    """
    pass


array = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = 2

nth_most_rate(array, 7)
