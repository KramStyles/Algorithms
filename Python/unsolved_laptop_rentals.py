def solution(times):
    laptops = 1
    highest = times[0][1]

    for idx, arr in enumerate(times):
        if (idx + 1) < len(times):
            first1 = arr[1]
            first2 = times[idx + 1][0]
            if first1 > first2 and first1 >= highest:
                laptops += 1
                highest = first1
    return laptops


arr1 = [[1, 5], [5, 6], [6, 7], [7, 9]]  # 1
arr2 = [[0, 4], [2, 3], [2, 3], [2, 3]]  # 4
arr3 = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]  # 3
arr4 = [[]]  # 0
arr5 = [[0, 5], [2, 4], [4, 7], [5, 7], [9, 20], [3, 15], [6, 10]]
arr6 = [[5, 6], [4, 5], [3, 4], [2, 3], [1, 2]]

solution(arr2)
