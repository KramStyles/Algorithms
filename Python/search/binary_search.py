def binary_search(lst, word):
    """
    Binary Search: This algorithm requires the file to be sorted in ascending or descending
    order. It searches for the target string by repeatedly dividing the search interval in
    half until the target string is found. This algorithm is efficient for large files, but
    requires the file to be sorted.

    lst: List of iterable values
    word: Statement to search for in lst
    """
    lst = sorted(lst)
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == word:
            print(f"Found: {word} in Binary Search")
            return mid
        elif lst[mid] < word:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Couldn't Find: {word} in Binary Search")
    return -1  # If the value is not found in the list
