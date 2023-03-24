def backspaceCompare(s: str, t: str) -> bool:
    arr1 = []
    arr2 = []
    for alp in s:
        if arr1 and alp == "#":
            arr1.pop()
        elif alp != "#":
            arr1.append(alp)
    for alp in t:
        if arr2 and alp == "#":
            arr2.pop()
        elif alp != "#":
            arr2.append(alp)

    return arr1 == arr2


s = "y#fo##f"
t = "y#f#o##f"

backspaceCompare(s, t)
print(s[-1], s[-2], s[-3])
