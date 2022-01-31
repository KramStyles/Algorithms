def fibonacci(n):
    ans = 0
    while n > 0:
        ans += n
        n -= 1
    return ans



def recursiveFibonacci(n):
    while n > 0:
        return n + (recursiveFibonacci(n-1))

print(recursiveFibonacci(3))