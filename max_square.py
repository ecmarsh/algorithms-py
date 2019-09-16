# 221. Maximal Square (DP)
#
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.
#
# Example:
# Input:
#   1 0 1 0 0
#   1 0 1 1 1
#   1 1 1 1 1
#   1 0 0 1 0
# Output: 4

# Analysis:
# M = len(rows), N = len(cols)
# Time: O(M*N)
# Space: O(N) <-- O(2N) one for cur, one for prev
#
# Alternative solution analysis:
# Brute force (check all possible squares): (MN)^2 time, constant space
# Entire dp table: O(MN) time, O(MN) space


class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        if len(grid) == 1:
            return max(grid[0])
        if len(grid[0]) == 1:
            return max([row[0] for row in grid])

        rows, cols = len(grid), len(grid[0])
        dp = [int(s) for s in grid[0]]
        max_side = max(0, dp[0])

        for r in range(1, rows):
            row = grid[r][:1] + [0] * (cols - 1)  # First col always grid val
            max_side = max(max_side, row[0])  # Check in case cur max is 0
            for c in range(1, cols):
                if grid[r][c] == '1':
                    left, up, diag = row[c-1], dp[c], dp[c-1]
                    row[c] = min(left, up, diag) + 1
                    max_side = max(row[c], max_side)
            dp = row

        return max_side * max_side
