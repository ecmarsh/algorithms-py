""" 1200. Minimum Absolute Difference (Contest 155)

Given an array of distinct integers arr, find all pairs of elements
with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs),
where each pair [a, b] follows:
 - a, b are from arr
 - a < b
 - b - a equals to the minimum absolute difference of any two elements in arr

Constraints:
 - `2 <= arr.length <= 10^5`
 - `-10^6 <= arr[i] <= 10^6`

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. 
             List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


Analysis:
N is len(arr)
Time: O(N log N) sort + O(N^2) to compare pairs = O(N^2 + NlogN)
Space: O(1)
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort(reverse=True)
        res, best = [], float('inf')
        for i in range(len(arr) - 1, 0, -1):
            j = i - 1
            while abs(arr[i] - arr[j]) <= best and j >= 0:
              diff = abs(arr[j] - arr[i])
              if diff < best:
                res = [[arr[i], arr[j]]]
                best = diff
              elif diff == best:
                res.append([arr[i], arr[j]])
              j -= 1
        return res

