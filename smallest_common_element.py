""" 1198. Find Smallest Common Element in All Rows

Given a matrix mat where every row is sorted in increasing order,
return the smallest common element in all rows.

If there is no common element, return -1.

Constraints:
    - i <= mat.length, mat[i].length <= 500
    - 1 <= mat[i][j] <= 10^4
    - mat[i] is sorted in ascending order


Example 1:
Input: mat=
[
    [1,2,3,4,5],
    [2,4,5,8,10],
    [3,5,7,9,11],
    [1,3,5,7,9]
]
Output: 5


Analysis:
M=len(mat), N=mat[i].length
Time: O(M * N) worst case if no common element in arr
Space: O(M * N) worst case if no common elements among any rows
"""

from collections import defaultdict


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Keep frequency count of elements in all rows.
        If frequency is the number of rows, val is smallest common since sorted.
        """
        rows, cols = len(mat), len(mat[0])
        freqs = defaultdict(int)
        for c in range(cols):
            for row in mat:
                val = row[c]
                freqs[val] += 1
                if freqs[val] == rows:
                    return val
        return -1

