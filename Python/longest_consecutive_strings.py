def longest_consec(strarr, k):
    word = ''
    for x in range(len(strarr)):
        if x+k <= len(strarr):
            newword = ''
            for y in range(k):
                newword += strarr[x+y]
            if len(newword) > len(word):
                word = newword
    return(word)