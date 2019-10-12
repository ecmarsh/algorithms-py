"""
739. Daily Temperatures

Given a list of daily temperatures T, return a list such that for each day,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

Constraints:
    - 1 <= len(temperatures) <= 30,000
    - 30 <= temperatures[i] <= 100

Example:
   Input: [73, 74, 75, 71, 69, 72, 76, 73]
   Output: [1, 1, 4, 2, 1, 1, 0, 0]

Analysis:
    Time: O(N) each index is visited at most twice
    Space: O(N) for output, O(1) otherwise
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n, right_max = len(T), T[-1] 
        ret = [0] * n
        for i in range(n-2,-1,-1):
            if T[i] >= right_max:
                # Just update the max seen if higher
                right_max = T[i]
            else:
                # Since we know theres a larger temp right
                # check right until find next warmest temperature. 
                days = 1
                while T[i+days] <= T[i]:
                    # Time save is here.
                    # We can skip indices already checked since we know
                    # if ret[day] waited some days and that day is
                    # less than current day (were in loop), the next
                    # warmer temperature is at least that index + wait days ahead.
                    days += ret[i+days] 
                ret[i] = days
        return ret

    def dailyTemperaturesAlt(self, T: List[int]) => List[int]:
        """
        Most common stack based solution. Still O(N) time but O(N) space.
        """
        n, stack = len(T), []
        ret = [0] * n
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                j = stack.pop()
                ret[j] = i - j
            stack.append(i)
        return ret
