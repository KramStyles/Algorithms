def solution(columnTitle: str) -> int:
    # Generate all the alphabets in uppercase
    from string import ascii_uppercase as alpha

    if len(columnTitle) > 1:
        # To get the index of each character
        total = [alpha.index(char) + 1 for char in columnTitle]
        
        total.reverse()
        # Todo: Error in Logic
        for x in range(len(total)):
            total[x] += (x * 26)
            print(x, total[x])
        return total
    else:
        return alpha.index(columnTitle) + 1
    
    

# print(solution('AB'))
print(solution('AZ'))
print(solution('BA'))
# print(solution('ZY'))