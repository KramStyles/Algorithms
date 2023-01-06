def log_search(search2, item):

    search_copy = search2[:]
    len_search = (len(search2)) // 2
    counter = 0
    while len_search > 1:
        counter += 1
        len_search = (len(search2)) // 2
        first = search2[:len_search]
        last = search2[len_search:]
        if item < search2[len_search]:
            search2 = first
        elif item > search2[len_search]:
            search2 = last
        elif item == search2[len_search]:
            return f"index:{search_copy.index(item)}, count:{counter}"
    if item != search2[0]:
        return f"index:-1, count:{counter}"
    return f"index:{search_copy.index(item)}, count:{counter}"


search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
search2 = [0, 5, 10, 15, 20, 25, 30, 35, 40]
print(log_search(search2, 15))
