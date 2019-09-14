# 287. Find the Duplicate Number
#
# Given an array nums containing n + 1 integers where
# each integer is between 1 and n (inclusive).
# 1. Prove there is at least one duplicate number must exist.
# 2. Assuming there is only one duplicate number, find the duplicate.

# Example 1:
# Input: [1,3,4,2,2]
# Ouput: 2

# Example 2:
# Input: [3,1,3,4,2]
# Output: 3

# Constraints:
# 1. You must not modify array. (Array is read only).
# 2. You must use only constant, O(1), extra space.
# 3. Runtime should be less than O(n^2).
# 4. Duplicate in array could be repeated more than once.


# Analysis
# Space: O(1)
# Time: O(μ + ƛ)
# μ = reptitions to find intersection (first while loop)
# ƛ = shortest cycle (index of first occurence of dup in arr)
# See: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Proof of duplicate with pigeonhole principle:
#    https://en.wikipedia.org/wiki/Pigeonhole_principle

# Solution uses same principle of finding intersection entry point of list:
# https://github.com/ecmarsh/algorithms/blob/master/exercises/listCycle.js

# Tortoise/Hare Explanation:
#   start-----entry-------
#               |        |
#               --------meeting point
#   x: distance from start to entry
#   y: distance from entry to meeting point
#   c: cycle length
#
#   When tortoise == hare at meeting point,
#     tortoise traveled: x + y,
#     hare traveled: x + y + n#c (which is x + y + loops inside the circle)
#
#   Since hare is twice faster than tortoise, so
#     2(x + y) = x + y + n#c
#
#   Then we can get
#     x = n#c - y
#     x = (n-1)#c + (c-y)
#
#   Which means
#     - traveling from start to entry (distance is x) and
#     - traveling from meeting point to entry (c-y + several loops in circle)
#     - will finally meet at entry, which is the duplicate
