def solution(columnTitle: str) -> int:
    # Generate all the alphabets in uppercase
    from string import ascii_uppercase as alpha

    if len(columnTitle) > 1:
        # To get the index of each character
        total = [alpha.index(char) + 1 for char in columnTitle]
        
        for x in range(len(total)-1, -1, -1):
            # total[x] += (x * 26)
            print(total[x], x)
        # return sum(total) - 1
        return total
    else:
        return alpha.index(columnTitle) + 1
    
    

# print(solution('AB'))
# print(solution('A'))
# print(solution('Z'))
print(solution('AZ'))
print(solution('BA'))
print(solution('ZY'))