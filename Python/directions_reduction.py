def dirReduc(arr):
    """
    Write a function dirReduc which will take an array of strings and returns an array of
    strings with the needless directions removed (W<->E or S<->N side by side).
    """
    direction = []
    oppo = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    for idx in range(len(arr)):
        if idx == 0:
            direction.append(arr[idx])
        else:
            # last = direction[-1]
            last1 = oppo[arr[idx]]
            if direction and direction[-1] == oppo[arr[idx]]:
                direction.pop()
            else:
                direction.append(arr[idx])
    return direction


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # '[WEST]'
u = ["NORTH", "WEST", "SOUTH", "EAST"]

dirReduc(u)
