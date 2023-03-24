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
    if num > 1:
        # Get numbers that can divide num
        # numbers = [dig for dig in range(2, num // 2) if num % dig == 0]
        for dig in range(2, num // 2 + 1):
            if num % dig == 0:
                ans = 0
                counter = 1
                while ans < num:
                    ans = dig**counter
                    if ans == num:
                        return [dig, counter]
                    else:
                        counter += 1
            return None
    # if numbers:
    #     # Get numbers that can divide num
    #     length = len(numbers) + 2
    #     numbers.pop()
    #     # for x in range(1, length + 1):
    #     return numbers
    else:
        return None

    #     for i in range(2, int(n**.5) + 1):
    #     number = n
    #     times = 0
    #     while number % i == 0:
    #         number /= i
    #         times += 1
    #         if number == 1:
    #             return [i, times]
    # return None

    # if (num)**(0.5) == int((num)**(0.5)):


# solution(81)
print(solution(4))
