def is_square(n):
    import math
    # This takes in a number and determines if it's a perfect square  
    return True if not math.sqrt(abs(n)) % 2 else False