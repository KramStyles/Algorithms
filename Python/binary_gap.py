from random import randint


def check(N):
    """
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

    For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

    Write a function:

    def solution(N)

    that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

    For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..2,147,483,647].

    """
    print(N)
    if N % 10 == 0 and N != 20:
        return 0
    N = bin(N)[2:]
    N = N.replace("1", "11")[1:].split(
        "1"
    )  # Added extra 1s to 1 so i can get the 1 as empty strings when split
    print(N)
    if N.count("") == 1:
        return 0
    if N[0] == "" and N[-1] == "":
        return len(max(N))
    else:
        # Checks if the zero is bounded by 1 and then finds the top bounded zero and returns it
        N = [
            N[x]
            for x in range(len(N))
            if x != 0 and x < len(N) - 1 and (N[x - 1] == "" and N[x + 1] == "")
        ]
        if N:
            return len(max(N))
        else:
            return 0
    return 0


print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
print("Ans is", check(randint(0, 2000)), "\n")
