def invert(lst):
    # return [-abs(num) if num > 0 else abs(num) for num in lst]
    # shorter solution
    return [-num for num in lst]
