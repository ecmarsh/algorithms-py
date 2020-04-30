"""
@lc id=1422 lang=python3 tag=string,contest

[1422] Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Constraints:
  - 2 <= s.length <= 500
  - The string s consists of characters '0' and '1' only.

Example 1:
  Input: s = "011101"
  Output: 5 
  Explanation: 
  All possible ways of splitting s into two non-empty substrings are:
  left = "0" and right = "11101", score = 1 + 4 = 5 
  left = "01" and right = "1101", score = 1 + 3 = 4 
  left = "011" and right = "101", score = 1 + 2 = 3 
  left = "0111" and right = "01", score = 1 + 1 = 2 
  left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
  Input: s = "00111"
  Output: 5
  Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
  Input: s = "1111"
  Output: 3


Complexity:
  Time: O(N) - N for total ones count, N for iteration = 2N
  Space: O(1) - implementation is O(N) because s[1:-1] creates copy, but could use a range loop and index instead at cost of more code.
"""

import collections


class Solution:
    def maxScore(self, s: str) -> int:
        zeros = int(s[0] == '0')
        total_ones = collections.Counter(s)['1'] - 1 + zeros  
        max_score = zeros + total_ones
        
        for n in s[1:-1]:
            if n == '0': 
                zeros += 1
            else:
                total_ones -= 1
            score = zeros + total_ones
            max_score = max(max_score, score)
        
        return max_score 
