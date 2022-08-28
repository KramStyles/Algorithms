"""
'2-4, 4-1' are matching tiles because the left is the same as the right
of the next tile
"""

case = "1 - 1,3 - 5,5 - 2,2 - 3,2 - 4"
def solution(case):
    case = case.split(',')
    count = 1
    for idx, item in enumerate(case):
        if idx < len(case)-1:
            if item[-1] == case[idx+1][0]:
                print(item[-1], case[idx+1][0])
                count += 1
                
    
    return print(count)
        

solution(case)