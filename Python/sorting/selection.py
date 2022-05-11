def solution(unsorted):
    """
        selection sort involves getting the minimun number and pushing it to the end of the list. 
        It can involve a new list
    """
    new_arr = []
    min_num = 0
    while len(unsorted) > 0:
        changed = False
        for num in range(len(unsorted) - 1):
            num1 = unsorted[num]
            num2 = unsorted[num + 1]
            if changed == False and num1 < num2:
                min_num = unsorted[num]
                changed = True
            elif changed == True and num1 < min_num:
                min_num = unsorted[num]
                
        new_arr.append(min_num)
        unsorted.remove(min_num)



solution([4, 6, 2, 7, 8, 7])