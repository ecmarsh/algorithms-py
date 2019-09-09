# 1186. Maximum Subarray Sum with One Deletion
# Weekly Contest 153 Submission

# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion.
# In other words, you want to choose a subarray and optionally delete one
# element from it so that there is still at least one element left and
# the sum of the remaining elements is maximum possible.
#
# Note that the subarray needs to be non-empty after deleting one element.
#
# Constraints:
#   1 <= len(arr) <= 10^5
#   -10^4 <= arr[i] <= 10^4

# Example 1:
# Input: [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2.

# Example 2:
# Input: [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.

# Example 3:
# Input: [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty.
#              You can't choose [-1] and delete -1 from it,
#              then get an empty subarray to make the sum equals to 0.

# Analysis for contest code:
# N = len(arr)
# Time: O(3N) --> O(N)
# Space: O(2N) --> O(N)

# Analysis for better solution:
# Time = O(N)
# Actual one pass, but since more checks, ends up being similar practical time.
# Space: O(1) <-- much better


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return arr[0]

        global_max = local_max = -10000  # see constraints

        # Store max seen at each index scanning 0...n
        # Track global_max for max w/o deletion
        pre = []
        for cur in arr:
            local_max = max(local_max + cur, cur)
            global_max = max(global_max, local_max)
            pre.append(local_max)

        # Store max seen at each index scanning n...0
        # Note we skip global_max calc since it would be the same.
        local_max = -10000
        suf = [None] * n
        for i, cur in enumerate(reversed(arr)):
            local_max = max(local_max + cur, cur)
            suf[n-1-i] = local_max

        # Update global_max if greater with deleted item
        for i in range(1, n-1):
            global_max = max(global_max, pre[i-1] + suf[i+1])

        return global_max


class BetterSolution:
    def maximumSum(self, arr: List[int]) -> int:
        """
        Optimal solution constant space and
        one pass using standard Kandanes
        """
        gmax = lmax = arr[0]
        ignored = not_ignored = 0
        for cur in arr:
            ignored = max(not_ignored, ignored + cur)
            not_ignored = max(cur, not_ignored + cur)
            gmax = max(gmax, ignored, not_ignored)
            lmax = max(lmax, cur)
        # if lmax is negative, all items are negative,
        # so just return the highest value
        return lmax if lmax < 0 else gmax
