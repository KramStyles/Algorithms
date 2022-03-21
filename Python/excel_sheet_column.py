def solution(columnTitle: str) -> int:
    # Generate all the alphabets in uppercase
    from string import ascii_uppercase as alpha

    if len(columnTitle) > 1:
        for char in columnTitle:
            print(alpha.index(char) + 1)
    else:
        return alpha.index(columnTitle) + 1
    
    

solution('AB')