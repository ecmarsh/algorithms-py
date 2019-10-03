"""
525. Max Length of Equal Contiguous Binary Array

Given a binary array, find the maximum length of
a contiguous subarray with equal number of 0's and 1's.

Constraints:
    - `0 <= len(nums) <= 50,000`


Example 1:
    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is longest with equal number of zeros and ones.

Example 2:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] or [1, 0] is longest with length of 2.


Analysis:
n is length of binary array
Time: O(n)
Space: O(n) worst case if all ones or all zeros for dict
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        ones_zeros_diff = 0
        diff_first_seen_index = {ones_zeros_diff: -1}
        for i, num in enumerate(nums):
            ones_zeros_diff += (num == 1) - (num == 0)  # 0->(-1), 1->(+1)
            diff_first_seen_index.setdefault(ones_zeros_diff, i)
            max_len = max(
                        max_len,
                        i - diff_first_seen_index.get(ones_zeros_diff))
        return max_len

