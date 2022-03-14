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


def upper_dec_arg(function):
    def wrapper(arg1, arg2):
        func = function(arg1, arg2)
        return f"{func} {arg1} {arg2}".upper()
    return wrapper

@upper_dec_arg
def simple_str(surname, name):
    return f"my name is"


# print(simple_str('michael', 'jamie'))

#     def enter_exit_info(self, func):
#         def wrapper(*arg, **kw):
#             print '-- entering', func.__name__
#             print '-- ', self.__dict__
#             res = func(*arg, **kw)
#             print '-- exiting', func.__name__
#             print '-- ', self.__dict__
#             return res
#         return wrapper

#     def enter_exit_info(func):
#         def wrapper(self, *arg, **kw):
#             print '-- entering', func.__name__
#             print '-- ', self.__dict__
#             res = func(self, *arg, **kw)
#             print '-- exiting', func.__name__
#             print '-- ', self.__dict__
#             return res
#         return wrapper

#     def enter_exit_info(func):
        
#         def wrapper(self, *arg, **kw):
#             print '-- entering', func.__name__
#             print '-- ', self.__dict__
#             res = func(self, *arg, **kw)
#             print '-- exiting', func.__name__
#             print '-- ', self.__dict__
#             return res
#         return wrapper

