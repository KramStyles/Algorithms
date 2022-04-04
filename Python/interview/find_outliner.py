def find_outlier(integers):
    """
        You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
        Write a method that takes the array as an argument and returns this "outlier" N.
    """
    evens = [num for num in integers if not num%2]
    odds = [num for num in integers if num%2]

    return evens[0] if len(evens)<len(odds) else odds[0]

def normal_divisors(integer):
    result = []
    for digi in range(2, (integer//2)+1):
        if not integer%digi:
            result.append(digi)

    return result

def divisors(integer):
    """
    Create a function named divisors that takes a non-negative integer 
    and returns an array with all of the integer's divisors 
    (except for 1 and the number itself). If the number is prime return an empty array.
    """

    result = [digi for digi in range(2, (integer//2)+1) if not integer%digi]
    return result
      

find_outlier([2,4,0,4,11,2602,36]) # 11
find_outlier([160,3,1719,19,13,-21]) #160

divisors(12) # [2, 3, 4, 5, 6]
divisors(13) # []
normal_divisors(25) # [5]