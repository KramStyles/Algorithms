def solution(numbers: list[int], target: int) -> list[int]:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
    find two numbers such that they add up to a specific target number. 
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. 
    You may not use the same element twice.


    Your solution must use only constant extra space.   
    """

    # This solution works perfectly but it's time complexity can rule you out!
    # We will use Python 1-pointer or (2-pointer)
    for index, number in enumerate(numbers):
        holder = numbers[:]
        holder.remove(number)
        for num in holder:
            if number + num == target:
                return [index +  1, numbers.index(num, index + 1) + 1]


print(solution(numbers = [2,7,11,15], target = 9)) # [1, 2]
print(solution(numbers = [2,3,4], target = 6)) # [1, 3]
print(solution(numbers = [0,0,3,4], target = 0)) # [1, 2]