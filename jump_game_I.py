# 55. Jump Game

# Given an array of non-negative integers,
# you are initially positioned at the first index of the array.
#
# Each element in the array represents the max number of indices
# you may "jump" from that position.
#
# Determine if you are able to reach the last index.

# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation:
#   You will always arrive at index 3 no matter what.
#   Its maximum jump length is 0, which makes it impossible
#   to reach the last index.

# Analysis:
# N is len(arr)
# Time: O(N)
# Space: O(1)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Loop through nums and store the farthest we can reach.
        If the farthest is gte last index, we can reach the end.
        """
        if len(nums) <= 1:
            return True

        farthest = 0

        for i, n in enumerate(nums):
            if farthest < i:
                return False  # We can't reach this position
            farthest = max(farthest, i + n)

        return farthest >= len(nums) - 1
