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

print(anagrams2('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams1('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))

