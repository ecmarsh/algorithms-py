"""
@lc id=1272 lang=python3 tag=linesweep,interval

[1272] Remove Interval
~ Biweekly Contest 14 ~

Given a sorted list of disjoint intervals,
each interval intervals[i] = [a, b] represents
the set of real numbers x such that a <= x < b.

We remove the intersections between any interval
in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

Constraints:
  - `1 <= intervals.length <= 10^4`
  - `-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9`


Example 1
Input:
  intervals = [[0,2],[3,4],[5,7]]
  toBeRemoved = [1,6]
Output:
  [[0,1],[6,7]]

Example 2
Input:
  intervals = [[0,5]]
  toBeRemoved = [2,3]
Output:
  [[0,2],[3,5]]


Complexity
Time: O(n), where n is number of intervals
Space: O(n) output: O(2n) worst case if each interval split.
"""


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        beg, end = toBeRemoved
        res = list()
        for a, b in intervals:
            # interval within toBeRemoved
            if a >= beg and b <= end:
                continue
            # toBeRemoved disjoint from interval
            if a >= end or b <= beg: 
                res.append([a, b])
            # lower portion of interval valid
            elif a < beg and b <= end: 
                res.append([a, beg])
            # upper portion of interval valid
            elif a >= beg and a <= end and b > end: 
                res.append([end, b])
            # toBeRemoved partitions the interval
            elif a < beg and b > end: 
                res.append([a, beg])
                res.append([end, b])
        return res

