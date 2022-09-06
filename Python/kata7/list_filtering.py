def filter_list(l:list):
    """
    In this kata you will create a function that takes a list of non-negative 
    integers and strings and returns a new list with the strings filtered out.
    """
    # return [item for item in l if str(item).isdigit()] # only wants numbers
    return [item for item in l if type(item) == int]
