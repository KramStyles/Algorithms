def hash_table(lst, word):
    """
    Hash Table: This algorithm involves creating a hash table from the file, which allows for
    fast lookups of specific strings. It is fast and efficient for large files, but requires
    extra memory to store the hash table.

    lst: List of iterable values
    word: Statement to search for in lst
    """
    hash_table = {}
    for i in range(len(lst)):
        if lst[i] not in hash_table:
            hash_table[lst[i]] = i
    if word in hash_table:
        print(f"Found: {word} in Hash Table Search")
        return hash_table[word]
    else:
        print(f"Couldn't Find: {word} in Hash Table Search")
        return -1  # If the value is not found in the list
