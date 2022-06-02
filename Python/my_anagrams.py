"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
 For example:
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
Note for Go
For Go: Empty string slice is expected when there are no anagrams found.
"""
def anagrams(word, words):
    answer = []
    for wd in words:
        if len(word) == len(wd):
            count = 0
            for char in wd:
                if char in word:
                    count+=1
            if count == len(word):
                answer.append(wd)

    if answer:
        for chars in answer:
            for wd in word:
                if wd not in chars:
                    answer.remove(chars)
    return answer

def anagrams1(word, words):
    from collections import Counter
    counts = Counter(word)
    return [w for w in words if Counter(w) == Counter(word)]

def anagrams2(word, words):
    return [anagram for anagram in words if sorted(anagram) == sorted(word)]

# print(anagrams2('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# print(anagrams1('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# print(anagrams('laser', ['lazing', 'lazy',  'lacer']))

def anagram_check(text):
    if not text:
        return []

    lst = [text[0]]
    first = ''.join(sorted(text.pop(0)))
    initials = [first]
    
    while text:
        nxt = ''.join(sorted(text[0]))
        if first == nxt:
            text.pop(0)
        elif nxt in initials:
            text.pop(0)
        else:
            lst.append(text.pop(0))
            first = nxt
            initials.append(first)
    lst.sort()
    return print(lst)
            

codes = ['code', 'doce', 'ecod', 'framer', 'frame']
code1 = ['code', 'aaagmnrs', 'anagrams', 'doce'] # anagrams, code
code2 = ['poke', 'pkoe', 'okpe', 'ekop'] # poke
# anagram_check(codes)
# anagram_check([])
# anagram_check(code2)

test1 = [1, 1, 2, 2, 3, 3] # k = 1 , 2
test2 = [1, 2, 5, 6, 9, 10] # k = 2, 0

def countPairs(numbers, k):
    numbers = set(numbers)
    count = 0
    for num in numbers:
        if (num + k) in numbers and (num + k) != num and :
            print(num, num + k)
            count += 1
    print(count)


# countPairs(test1, 1)
# countPairs(test2, 2)
countPairs([1, 2, 3, 4], 0)