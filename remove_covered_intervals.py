"""
@lc id=1288 lang=python3 tag=intervals,contest

[1288] Remove Covered Intervals
  Biweekly Contest 15

Given a list of intervals, remove all intervals that are
covered by another interval in the list.

Interval [a,b) is covered by interval [c,d)
if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

Constraints:
  - `1 <= intervals.length <= 1000`
  - `0 <= intervals[i][0] <= intervals[i][1] <= 10^5`
  - intervals[i] != intervals[j] for all i != j


Example 1:
  Input: intervals = [[1,4],[3,6],[2,8]]
  Output: 2
  Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.


Complexity:
  Let: N = number of intervals
  Time: O(N^2). Every interval pair is compared.
  Space: O(1).
"""


from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda A: A[1]-A[0])
        count=len(intervals)

        for i, A in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                B = intervals[j]
                if B[0] <= A[0] and B[1] >= A[1]:
                    count -= 1
                    break

        return count

