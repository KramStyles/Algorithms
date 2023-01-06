# def solution(message, K):
#     # write your code in Python 3.6
#     msg = message.split(' ')
#     new_msg = msg[0]

#     if len(new_msg) > K: return ""

#     for idx in range(1, len(msg)):

#         joined = f"{new_msg} {msg[idx]}"
#         length = len(joined)
#         if len(joined) <= K:
#             new_msg = joined
#         # else: break
#         else: return new_msg

#     print(new_msg, 'answer')

# txt = "Codility We test coders"
# txt2 = "The quick brown fox jumps over the lazy dog"
# txt3 = "Why not"
# txt4 = "To crop or not to crop"

# solution(txt, 12)

# p1 = [1, 4, 1]
# s1 = [1, 5, 1]

# p2 = [4, 4, 2, 4]
# s2 = [5, 5, 2, 5]

# p3 = [2, 3, 4, 2]
# s3 = [2, 5, 7, 2]

# def solution2 (P, S):
#     seats = sorted(S, reverse=True)
#     people = sum(P)

#     seat = 0
#     while people > 0:
#         people -= seats[seat]
#         seat += 1

#     print(seat)


# solution2(p3, s3)

# def solution3(A):
#     A.sort()
#     target = sum(A) / 2
#     poll = sum(A)

#     while poll > target:
#         if A[0] < A[1]:
#             value = A.pop(0)
#             start = 0
#             end = len(A)

#             middle = (start + end) // 2
#             while A[middle] != value:
#                 if start != end and A[middle] > value and A[middle + 2] < value:
#                     A.insert(middle, value)
#                     break
#                 if A[middle] > value:
#                     start = middle
#                 elif A[middle] < value:
#                     end = middle
#                 elif start == end and A[middle]

# def solution(A):
#     poll = sum(A)
#     target = poll / 2
#     count = 0
#     while poll > target:
#         maxi = max(A)
#         poll -= maxi / 2
#         A[A.index(maxi)] = maxi / 2
#         count += 1
#     return count

# solution([1,2,3,4,5])


def numberOfCarryOperations(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    result = 0
    holding = [0]
    if num2 > num1:
        big = num2
        small = num1
    else:
        big = num1
        small = num2
    nums = [str(big)[::-1], str(small)[::-1]]
    for i in range(len(nums[1])):
        print(int(nums[0][i]) + int(nums[1][i]) + holding[-1])
        if int(nums[0][i]) + int(nums[1][i]) + holding[-1] >= 10:
            result += 1
            holding.append(1)

    return result


print(numberOfCarryOperations(1, 999999))
