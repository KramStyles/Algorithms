def upper_dec(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper()

def simple_string():
    return "i am a python developer"

print(upper_dec(simple_string))