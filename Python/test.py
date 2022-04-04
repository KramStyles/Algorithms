count = 8
for x in range(1, count):
    count -= 1
    space = '-'*count
    ha = '#' * x
    print(space,ha, ' ', ha, space)