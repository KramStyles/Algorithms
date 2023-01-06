def split_integer(num, parts):
    answer = divmod(num, parts)
    checks = ((str(answer[0]) + " ") * parts).split()
    ans = [int(x) for x in checks]
    if answer[1] > 0:
        for x in ans:
            if sum(ans) < num:
                ans.append(x + 1)
                ans = ans[1:]
    return ans


query = {"capacity": 2, "hotel_id": 1}
rooms = {
    1: {"hotel_id": 2, "price": 4000, "capacity": 3, "_id": 1},
    2: {"hotel_id": 1, "price": 3000, "capacity": 2, "_id": 2},
    3: {"hotel_id": 2, "price": 3000, "capacity": 2, "_id": 3},
}

lst = []
for num in rooms:
    count = 0
    for key in query.keys():
        if query[key] == rooms[num][key]:
            count += 1
    if count == len(query.keys()):
        lst.append(rooms[num])
        # print(key, query[key])
        # print(key, rooms[num][key])


conditions = query


class self:
    pass


self.data = rooms
for query in conditions:
    answer = [
        self.data[x]
        for x in self.data
        if query in self.data[x] and conditions[query] == self.data[x][query]
    ]

# print(lst)
print(answer)
