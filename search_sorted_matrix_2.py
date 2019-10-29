"""
@=lc id=240 lang=python3 tag=matrix,search

[240] Search a Sorted 2D Matrix II

Write an efficient algorithm that searches for a value in an
m x n matrix. This matrix has the following properties:
    * Ints in each row are sorted in ascending left->right.
    * Ints in each column are sorted in ascending top->bottom.

Example:
[
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
Given target=5, return true.
Given target=20, return false.
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Psuedo:
        Start from 1st row, last column, then
        proceed top->down, right-left based on decisions.

        Decisions:
        1. Target Found
            m[r][c] == target --> TRUE (or location in variants)
        2. Target is greater than current, eliminate entire row
            m[r][c] < target --> row++
        3. Target less than current, eliminate entire column
            m[r][c] > target --> col--
        Termination: End when nothing left to search
            row > lastRow OR col < 0 --> FALSE

        Complexity:
        * Each iteration, we eliminate either a row or a column.
        * Worst case is element does not exist value close to last row column.
        * In which case we search m+n-1 locations, so:
            * Time: O(m+n)
            * Space is O(1)
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1
        
        while r < rows and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            if val < target:
                r += 1
            else:
                c -= 1
        
        return False
