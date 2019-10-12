"""
213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this
place are arranged in a circle. That means the first house is the neighbor
of the last one. Meanwhile, adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were
broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight
without alerting the police.


Example 1:
    Input: [2,3,2]
    Output: 3
    Explanation: House 0 and house 2 are adjacent, so cannot rob both.

Example 2:
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 0 then house 2 for 1 + 3 = 4.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Same as House Robbers I, solved here:
        https://github.com/ecmarsh/algorithms/blob/master/exercises/robMaxMoney.js
        Except now we are constrained on robbing house 1 based on house n.
        That is, we must break the circle by assuming a house isn't robbed.
        To find out which one, we must try NOT robbing first 2 houses:
            1) skip house[0], allowing us to rob house[-1], or
            2) skip house[1], allowing us to rob house[-2]
        We can use the same solution in house robbers 1, but restrict our range
        The answer is, of course, is which 2 skips leads to the greater money.
        Let n = len(nums), then:
            T(n) = (n-2) + (n-2) = 2n-4 = O(n)
            S(n) = O(1)
        """
        # can only rob 1 house since 3 houses are all adjacent
        if len(nums) <= 3:
            nums.append(0)  # handle no houses
            return max(nums)

        op1, op2 = 0, 0

        # op1: house[0]..house[n-2]
        n1, n2 = 0, nums[0]
        for i in range(1, len(nums)-1):
            n1, n2 = n2, max(n1 + nums[i], n2)
        op1 = n2

        # op2: house[1]..house[n-1]
        n1, n2 = 0, nums[1]
        for i in range(2, len(nums)):
            n1, n2 = n2, max(n1 + nums[i], n2)
        op2 = n2

        return max([op1, op2])
