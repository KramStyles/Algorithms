def solution(columnTitle: str) -> int:
    # Generate all the alphabets in uppercase
    from string import ascii_uppercase as alpha

    if len(columnTitle) > 1:
        # To get the index of each character
        total = [alpha.index(char) + 1 for char in columnTitle]
        
        total.reverse()
        for x in range(len(total)):
            total[x] += (x * 26)
        return sum(total) - 1
    else:
        return alpha.index(columnTitle) + 1
    
    

print(solution('AB'))
print(solution('A'))
print(solution('Z'))
print(solution('ZY'))