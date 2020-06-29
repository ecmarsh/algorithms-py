"""
@lc id=62 lang=python3 tag=dp,state,machine

[62] Unique Paths

A robot is located at the top-left corner of a m x n grid. (0,0)

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Constraints:
  - 1 <= m, n <= 100
  - It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

Example 1:
  Input: m = 3, n = 2
  Output: 3
  Explanation:
    From the top-left corner, there are a total of 3 ways to
    reach the bottom-right corner:
      1. Right -> Right -> Down
      2. Right -> Down -> Right
      3. Down -> Right -> Right

Example 2:
  Input: m = 7, n = 3
  Output: 28

Complexity:
  Time: O(m x n)
  Space: 2M -> O(m) using only previous and current row
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        At each point in the grid, store the total 
        number of ways to get to the current cell,
        either from the left, or up, since the robot
        can only move right or down.
        The final square will hold the total number of unique paths.
        Note: We could also store only two rows at a time to reduce space. 
        """
        grid = [[0 for _ in range(0, m)] for _ in range(0, n)]
        grid[0][0] = 1

        for r in range(0, n):
            for c in range(0, m):
                if (r - 1) >= 0:  
                    grid[r][c] += grid[r-1][c]
                if (c - 1) >= 0:
                    grid[r][c] += grid[r][c-1] 

        return grid[n-1][m-1]
