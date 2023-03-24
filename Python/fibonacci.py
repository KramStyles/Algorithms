def fibonacci(n):
    ans = 0
    while n > 0:
        ans += n
        n -= 1
    return ans


def recursiveFibonacci(n):
    if n > 0:
        ans = n + recursiveFibonacci(n - 1)
    else:
        return False
    return ans


print(recursiveFibonacci(5))
