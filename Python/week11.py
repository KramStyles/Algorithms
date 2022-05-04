def searchinsortedmatrix(matrix,target):
    for idx, item in enumerate(matrix):
        for idx2, value in enumerate(item):
            if value == target:
                print(value,idx, idx2)
                return [idx, idx2]
    return [-1, -1]

mat = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]

# searchinsortedmatrix(mat, 45)

def longest_substring_without_duplication(string):
    holder = []
    general = []

    while string:
        for chars in string:
            if chars not in holder:
                holder.append(chars)
            else: break
        general.append(''.join(holder))
        holder = []
        string = string[1:]
    
    print(max(general, key=len))
    return max(general, key=len)

string1 = 'clementisacap'
string2 = 'decadevsindecagonarelit'
string3 = 'abcdeabcdefc'

longest_substring_without_duplication(string1) # 'mentisac
longest_substring_without_duplication(string2)
longest_substring_without_duplication(string3)