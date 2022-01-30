test = "aaaabbcdefffffffg"
# ["aa[aa]bbcdeff[fffff]g", 2]

def isolate(duplicates):
    words = []
    initial = []
    hold = ""
    counter = 0
    # For loop to get the uniques of the letters
    for x in duplicates:
        if x not in initial:
            initial.append(x)
    # Loop to get similar characters in a single array
    for x in initial:
        for char in duplicates:
            if char == x:
                hold += x
        words.append(hold)
        hold = ""
    # Loop to arrange them in patterns
    for x in words:
        if len(x) > 2:
            hold += f"{x[:2]}[{x[2:]}]"
            counter += 1
        else:
            hold += x

    return [hold, counter]


print(isolate("aaasssssssddddffgkkkkkuueyyryrhhsgfhjjsnnnnnnjjfmgjghjdjjjjdhyteghsjckjdheyebnfjhhgnjdfyfggbejjwtyjfjcbdgdhdjfjeeebddhdychdjdjmkj"))