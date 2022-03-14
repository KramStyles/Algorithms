def solution(num):
    """
    Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) 
    and (9,2) are valid solutions. However, the tests take care of this, 
    so if a number is a perfect power, return any pair that proves it.

    Examples
    isPP(4) => [2,2]
    isPP(9) => [3,2]
    isPP(5) => None

    """
    # Make sure it's not a prime number
    check = True
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                check = False
    if check:
        print(num, 'is a prime number')


# solution(81)
solution(97)
