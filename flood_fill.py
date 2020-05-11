"""
@lc id=733 lang=python3 tag=array,dfs

[733] Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Constraints:
  - The length of image and image[0] will be in the range [1, 50].
  - The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
  - The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

Example:
  Input:  image = [[1,1,1],[1,1,0],[1,0,1]]
          sr = 1, sc = 1, newColor = 2
  Output: [[2,2,2],[2,2,0],[2,0,1]]
  Explanation:
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Complexity:
  Time: O(n) where n is number of pixels in the image
             -> worst case if all of the pixels are the old color.
  Space: O(n) n-1 pixels all pixels could be added if all old color
"""

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        rows, cols = len(image), len(image[0])
        image[sr][sc] = newColor
        stack = [(sr, sc)]
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        while stack:
            y, x = stack.pop()
            for dy, dx in moves:
                r, c = (y + dy), (x + dx)
                if 0 <= r < rows and 0 <= c < cols and image[r][c] == oldColor: 
                    image[r][c] = newColor
                    stack += [(r, c)]

        return image
