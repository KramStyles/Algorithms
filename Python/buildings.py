def sunsetViews(building, direction):
    """
    The input array named buildings contains positive, non-zero integers representing the heights of the buildings. A building at index i thus has a height denoted by buildings[i]. All of the buildings face the same direction, and this direction is either east or west, denoted by the input string named direction, which will always be equal to either "EAST" or "WEST". In relation to the input array, you can interpret these directions as right for east and left for west.

    Important note: the indices in the ouput array should be sorted in ascending order.
    Sample Input #1
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "EAST" // -> Right

    Sample Output #1
    [1, 3, 6, 7] // The indexes of the buildings that can see the Sun

    As shown in the image above, with the building's height and their indexes, only the buildings that have a clear view in the East direction are returned. When the direction is WEST, the returned values are different.

    Sample Input #2
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "WEST" // <- Left

    Sample Output #2
    [0, 1]
    """
    if direction != "EAST":
        # To reverse the order of the building due to sun position
        building = list(reversed(building))

    seeing = []
    for index, build in enumerate(building):
        if index < len(building) - 1:
            # Gets the rest of the building and makes sure current building is higher than them
            remaining_buildings = building[index + 1 :]
            next_building = building[index + 1]
            if build > next_building and build > max(remaining_buildings):
                seeing.append(index)
        else:
            # The first building facing the sun is always seeing the sunlight
            seeing.append(index)

    if direction != "EAST":
        # To reverse the order of the results
        seeing = list(reversed(seeing))
        for index, build in enumerate(seeing):
            seeing[index] = len(building) - (build + 1)

    print(seeing)


sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST")
sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST")
