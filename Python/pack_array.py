def pack_array(integers: list) -> int:
    print(integers)
    for x in range(1, int(len(integers) / 2)):
        if x % 2:
            int_len = int(len(integers) / 2)
            for y in range(0, len(integers), 2):
                integers.append(integers[y] + integers[y + 1])
            integers = integers[-int_len:]
            print(integers)
        else:
            int_len = int(len(integers) / 2)
            for y in range(0, len(integers), 2):
                integers.append(integers[y] * integers[y + 1])
            integers = integers[-int_len:]
            print(integers)
    if len(integers) == 2:
        integers[0] = integers[0] * integers[1]
        print(integers)

    return integers[0]


print(pack_array([1, 2, 3, 4, 5, 6, 7, 8]))
print(pack_array([4, 4]))
print(pack_array([1, 1, 1, -1]))
