def normalFac(number):
    ans = 1
    while number > 0:
        ans *= number
        number -= 1
    return (ans)

def recursiveFactorial(number):
    if number > 0:
        ans =  (number + recursiveFactorial(number - 1))
        print(ans)
    else:
        return False
    return ans


print(recursiveFactorial(5))