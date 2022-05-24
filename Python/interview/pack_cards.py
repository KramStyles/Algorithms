card = [2, 3, 4, 5, 6, 7, 8, 9, 'jack', 'queen', 'king', 'ace']
temps = [[] for x in card]

result = []

query1 = [2, 6, 2, 9, 'ace', 'queen', 'king', 'king', 'ace', 5]

for item in query1:
    if temps[card.index(item)] == []:
        temps[card.index(item)] = [item]
    else:
        temps[card.index(item)].append(item)

for item in temps:
    if item:
        result.extend(item)
print(result)