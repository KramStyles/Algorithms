def linear_search(lst, word):
    """
    Linear Search: This is a simple algorithm that searches through each element of the file
    sequentially until it finds the target string. It is easy to implement but can be slow
    for large files.Linear Search: This is a simple algorithm that searches through each
    element of the file sequentially until it finds the target string.
    It is easy to implement but can be slow for large files.

    lst: List of iterable values
    word: Statement to search for in lst
    """
    for i in range(len(lst)):
        if lst[i] == word:
            print(f"Found: {word} in Linear Search")
            return i
    print(f"Couldn't Find: {word} in Linear Search")
    return -1  # If the value is not found in the list
