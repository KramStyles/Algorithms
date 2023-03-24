class Solution:
    def calPoints(self, ops: list[str]) -> int:
        total = []
        for item in ops:
            if item.isdigit() or item[0] == "-":
                total.append(int(item))
            elif item == "+":
                total.append(total[-1] + total[-2])
            elif item == "D":
                total.append(total[-1] * 2)
            elif item == "C":
                total.pop()
        return sum(total)

    # Just putting code here to meet the requirement for today


test2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]

sol = Solution()
sol.calPoints(test2)
