def normalFac(number):
    ans = 1
    while number > 0:
        ans *= number
        number -= 1
    return ans


def recursiveFactorial(number):
    if number > 0:
        ans = number + recursiveFactorial(number - 1)
        print(ans)
    else:
        return False
    return ans


def theirRecursive(number):
    if number <= 0:
        return 1
    else:
        return number * theirRecursive(number - 1)


print(recursiveFactorial(5))
print(theirRecursive(5))
