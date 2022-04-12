def solution(arr, target):
    """
    Given a sorted array of integers arr and an integer target, find the index 
    of the first and last position of target in arr. If target can't be found,
    return '-1'
    """
    if target not in arr:
        return -1
    else:
        start, stop = 0, 0
        for idx, item in enumerate(arr):
            if item == target:
                start = idx
                stop = idx
                while arr[idx+1] == item:
                    stop += 1
                    idx += 1
                return [start, stop]

solution([2,4,5,5,5,5,5,7,9,9], 5)