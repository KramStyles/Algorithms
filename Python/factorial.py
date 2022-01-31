def normalFac(number):
    ans = 1
    while number > 0:
        ans *= number
        number -= 1
    return (ans)

def recursiveFactorial(number):
    if number > 0:
        return (number * recursiveFactorial(number - 1))
    else:
        return False


print(recursiveFactorial(5))