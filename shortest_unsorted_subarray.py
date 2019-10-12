"""
581. Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray
that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Constraints:
    - 1 <= len(nums) <= 10^4
    - A[i-1] <= A[i] for all sorted A[i]. (May be duplicates).

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order
             to make the whole array sorted in ascending order.

Analysis:
n is len(nums)
Time: O(n) (Can do in one pass too, but still need to check min/max)
Space: O(1)
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        An array is sorted if for all A[1:][i], A[i] > A[i-1]
        and for all A[:-1][j], A[j] < A[j+1].
        Going from left, the max value should always be the current index.
        Going from right, the min value should always be the current index.
        We're essentially looking for the longest left sorted subarray
        and longest right subarray. Our answer is in the middle.
        """
        if len(nums) == 1:
            return 0

        last, max_left = -1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] < max_left:
                last = i
            else:
                max_left = nums[i]

        if last == -1:
            return 0

        first, min_right = last-1, nums[last]
        for i in range(last-1, -1, -1):
            if nums[i] > min_right:
                first = i
            else:
                min_right = nums[i]

        return (last - first) + 1
