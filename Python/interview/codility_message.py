def solution(message, K):
    # write your code in Python 3.6
    msg = message.split(' ')
    new_msg = msg[0]

    if len(new_msg) > K: return ""

    for idx in range(1, len(msg)):
        each = msg[idx]
        joined = f"{new_msg} {msg[idx]}"
        length = len(joined)
        if len(joined) <= K:
            new_msg = joined
        else: break
        # print(idx)

    # for idx, item in enumerate(msg):
    #     if idx == 0 and len(item) < K:
    #         new_msg +=item
    #         K -= len(new_msg)
    #     else:
    #         if len(item) + 1 < K:
    #             new_msg = f"{new_msg} {item}"
    #             K -= len(item) + 1


    print(new_msg, 'answer')

txt = "Codility We test coders"
txt2 = "The quick brown fox jumps over the lazy dog"
txt3 = "Why not"
txt4 = "To crop or not to crop"

p1 = [1, 4, 1] 
s1 = [1, 5, 1]

p2 = [4, 4, 2, 4]
s2 = [5, 5, 2, 5]

p3 = [2, 3, 4, 2]
s3 = [2, 5, 7, 2]

def solution2 (P, S):
    seats = sorted(S, reverse=True)
    people = sum(P)

    seat = 0
    i = 0
    while people > 0:
        people -= seats[i]
        i += 1
        seat += 1

    print(seat)



# solution2(p3, s3)

def solution3(A):
    A.sort()
    target = sum(A) / 2
    poll = sum(A)

    while poll > target:
        if A[0] < A[1]:
            value = A.pop(0)
            start = 0
            end = len(A)

            middle = (start + end) // 2
            while A[middle] != value:
                if start != end and A[middle] > value and A[middle + 2] < value:
                    A.insert(middle, value)
                    break
                if A[middle] > value:
                    start = middle
                elif A[middle] < value:
                    end = middle
                elif start == end and A[middle]


