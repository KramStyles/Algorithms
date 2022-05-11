def bubble(unsorted_list):
    sort = False
    list_len = len(unsorted_list) - 1
    while not sort:
        sort = True
        for num in range(0, list_len):
            numb1 = unsorted_list[num]
            numb2 = unsorted_list[num+1]
            if numb1 > numb2:
                sort = False
                unsorted_list[num], unsorted_list[num+1] = numb2, numb1

    return unsorted_list

bubble([12, 1, 43, 29, 11, 23, 4, 21, 45, 7])

