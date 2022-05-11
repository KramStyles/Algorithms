def solution(column_title: str) -> int:
    # Generate all the alphabets in uppercase
    from string import ascii_uppercase as alpha

    if len(column_title) > 1:
        # To get the index of each character

        # total = [alpha.index(char) + 1 for char in columnTitle]
        
        # for x in range(len(total)-1, -1, -1):
        #     # total[x] += (x * 26)
        #     print(total[x], x)
        # # return sum(total) - 1
        # return total

        total = [alpha.index(char) + 1 for char in column_title]
        total.reverse()

        # List comprehension to solve problem
        # total = [total[num] * (26 ** num) if num > 0 else total[num] for num in range(len(total))]

        # Normal loop to solve issue!
        for num in range(len(total)):
            if num > 0:
                total[num] *= len(alpha) ** num
        return sum(total)

    else:
        return alpha.index(column_title) + 1


<<<<<<< HEAD
# print(solution('AB'))
# print(solution('A'))
# print(solution('Z'))
print(solution('AZ'))
print(solution('BA'))
print(solution('ZY'))
=======
if __name__ == '__main__':
    # print(solution('AB'))
    # print(solution('AA'))  # 27 [26 * 1, 1]
    # print(solution('AB'))  # 28 [26 * 1, 2]
    # print(solution('AZ'))  # 52 [26 * 1, 26]
    # print(solution('BA'))  # 53 [26 * 2, 1]
    print(solution('ZY'))  # 701 [26*26, 25]
    print(solution("FXSHRXW"))  # 2147483647 [6 * 26* 6, 24 * 26 * 5, 19 * 26 * 4, 8 * 26 * 3, 18 * 26 * 2, 24 * 26 * 1, 23])
>>>>>>> ed911911732b7d1121a502ad76d598e12a751eed
