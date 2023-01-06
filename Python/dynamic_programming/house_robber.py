class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain
        amount of money stashed, the only constraint stopping you from robbing each of them is that
        adjacent houses have security systems connected and it will automatically contact the police
        if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house, return the maximum
        amount of money you can rob tonight without alerting the police.

        Example 1:

        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
        Example 2:

        Input: nums = [2,7,9,3,1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.
        """
        # total = [0, 0]
        # for item in range(0, len(nums), 2):
        #     total[0] += nums[item]
        # for item in range(1, len(nums), 2):
        #     total[1] += nums[item]
        # return print(max(total))

        prev, nxt = 0, 0
        for num in nums:
            temp = max(num + prev, nxt)
            prev = nxt
            nxt = temp

        return nxt


soln = Solution()
nums = [1, 2]
nums1 = [1, 2, 3, 1]  # 4
nums2 = [2, 7, 9, 3, 1]  # 12
nums2 = [2, 1, 1, 2]  # 4

soln.rob(nums1)
soln.rob(nums2)
soln.rob(nums)
