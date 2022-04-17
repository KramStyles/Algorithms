def bubble(unsorted_list):
    sort = False
    list_len = len(unsorted_list) - 1
    while not sort:
        sort = True
        for num in range(0, list_len):
            
