
def high_order_bitmask(word_size: int) -> int:
    """
        Let's write a function called highOrderBitmask that, when given a word size in bits, 
        will return us the decimal value for the bitmask we'll need to extract the higher 
        order bits out of a word of that same bit size.

        In our example above, the word size was 8 bits and we wanted to extract 
        the most signficiant half or the left-most 4 bits.

        All given word sizes will be even. 
    """

    checks = word_size // 2
    binary = f"{'1'*checks}{'0'*checks}"
    return int(binary, 2)

# high_order_bitmask(2)
# high_order_bitmask(4)
# high_order_bitmask(8)

def high_and_low(numbers: str) -> str:
    """
        In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
        "1 2 3 4 5" 	"5 1"
        "1 2 -3 4 5" 	"5 -3"
        "1 9 3 4 -5" 	"9 -5"
    """
    numbers = [int(num) for num in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))