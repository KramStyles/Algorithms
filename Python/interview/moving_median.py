def MovingMedian(arr):
    result = ''
    n = arr.pop(0) - 1
    for i in range(len(arr)):
        if i > n:
            new = arr[i - n : i + 1]
        else:
            new = arr[:i + 1]
        new.sort()
        if len(new)%2:
            result += str(new[len(new)//2]) + ','
        else:
            result += str(sum(new[len(new)//2 - 1: len(new)//2 + 1])//2) + ','
    return result[:-1]
print(MovingMedian([3,1,3,5,10,6,4,3,1]))
print(MovingMedian([5,2,4,6]))
print(MovingMedian([3,0,0,-2,0,2,0,-2]))
