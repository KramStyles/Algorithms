def high_and_low(numbers):
    """
    In this little assignment you are given a string of space separated numbers, 
    and have to return the highest and lowest number.
    """
    numbers = numbers.split(" ")
    numbers = list(map(int, numbers))
    return f"{max(numbers)} {min(numbers)}"

print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"