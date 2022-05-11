import imp


def calPoints(ops):
    """
    Add number to list, 
    C => removes previous score
    D => Add 2 * previous
    + => Sum of previous 2 scores
    """
    result = []
    for num in ops:
        if num == 'C':
            if result != []:
                result.pop()
        elif num == 'D':
            if result != []:
                result.append(result[-1] * 2)
        elif num == '+':
            if result != []:
                result.append(sum(result[-2:]))
        else:
            result.append(int(num))

    
    return sum(result)

# calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) # 27

def checkBrackets(s):
    oppo = {
        '{': '}',
        '[': ']', 
        '(': ')',
        '}': '{',
        ']': '[', 
        ')': '('
    }
    group = []
    for x in s:
        if len(group) > 0 and oppo[group[-1]] == x:
            group.pop()
        else:
            group.append(x)
    # groups = [group.pop() if len(group) > 0 and oppo[group[-1]] == x else group.append(x) for x in s]
    if not group: return print('Valid')
    return print('Invalid')

# checkBrackets('()[]{}{{}}')

def c(S):
    from string import ascii_letters
    txt = []
    sym = {}
    for idx, s in enumerate(S):
        if s in ascii_letters:
            # txt.append(s)
            txt.insert(0,s)
        else:
            sym[idx] = s

    # txt.reverse()
    for s in sym:
        txt.insert(s, sym[s])

    print(''.join(txt))


c('a-bC-dEf=ghIj!!')