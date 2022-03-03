def upper_dec(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper()

def simple_str():
    return "i am a programmer"



# We can have more than one decorator acting on a function
def str_breaker(function):
    def wrapper():
        return function.split(' ')
    return wrapper()


@str_breaker
@upper_dec
def simple_str1():
    return "i am a programmer1"


print(upper_dec(simple_str))
print(simple_str1)