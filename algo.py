def reduce_directions(directions: list) -> list:

    """
    We are given directions to go from one point to another. The directions are "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going one direction and coming back the opposite direction is a wasted effort, so let's concise these directions to go the shortest route.

    For example, given the following directions:

    plan = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

    You can immediately see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place!
    So the task is to reduce a simplified version of the plan. A better plan in this case is simply:

    plan = ["WEST"]

    Other examples:
    In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing. The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).
    In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
    """
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}

    holder = directions[:]

    shorten = []
    for index, dir in enumerate(directions):
        # (shorten.pop()) if shorten and shorten[-1] == opposites[dir] else shorten.append(dir)
        if shorten and shorten[-1] == opposites[dir]:
            shorten.pop()
        else:
            shorten.append(dir)
    return shorten


test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]  # []
test1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # WEST

print(reduce_directions(test1))
