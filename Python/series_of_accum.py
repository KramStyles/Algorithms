def accum(s):
    """
    This challenge requires you to create a solution only based on the input and output to your function.

    The examples below show you how to write function accum
    'abcd' => 'A-Bb-Ccc-Dddd'
    'cWat' => 'C-Ww-Aaa-Tttt'
    """
    result = ""
    for idx, chars in enumerate(s):
        result += chars * (idx + 1)
        result = result.title() + "-"

    return result[:-1]


accum("abcd")
accum("cWat")


def palindrome_chain_length(n):
    """
    Number is a palindrome if it is the same when its digits are in reversed order. For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.

    Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. The special step is: reverse the digits and add this to the original number. If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.

    If the input number is already a palindrome, the number of steps is 0.

    Input will always be a positive integer.

    For example, if n is 87:
         87 +   78 =  165
        165 +  561 =  726
        726 +  627 = 1353
        1353 + 3531 = 4884
        Length = 4
    """
    rev = str(n)[::-1]
    steps = 1
    if n == int(rev):
        return 0
    n = n + int(rev)
    while str(n) != str(n)[::-1]:
        rev = str(n)[::-1]
        n = n + int(rev)
        steps += 1

    print(steps, n)


# palindrome_chain_length(87)
# palindrome_chain_length(10)
# palindrome_chain_length(89)
palindrome_chain_length(88)
palindrome_chain_length(7)
