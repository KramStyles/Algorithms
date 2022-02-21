def array_packing(integers: list) -> int:
    temp = integers[0]
    integers[0] = integers[-1]
    integers[-1] = temp
    numbs = [bin(x)[2:] for x in integers]
    # total = []
    # for x in numbs:
    #   zer = '0'*(8-len(x))
    #   total.append(zer+x)
     
    total = [('0'*(8-len(x))) + x for x in numbs]
    return int(''.join(total), 2)