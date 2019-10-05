"""
1167. Minimum Cost to Connect Sticks

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into
one stick by paying a cost of X + Y.  You perform this action
until there is one stick remaining.

Return the minimum cost of connecting all the
given sticks into one stick in this way.

Constraints:
    - 1 <= len(sticks) <= 10^4
    - 1 <= sticks[i] <= 10^4


Example 1:
    Input: [2,4,3]
    Output: 14
Example 2:
    Input: [1,8,3,5]
    Output: 30


Analysis:
N is len(sticks)
Time: O(N log N)
    - heapify O(N) + (N-1) x (pop (log N) + replace(log N)) = N + (N-1)*2logN
Space: O(1) extra space. Sticks is "heapified" in place.
"""


from heapq import heapify, heappop, heapreplace


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            m = heappop(sticks) + sticks[0]
            cost += m
            heapreplace(sticks, m)
        return cost
