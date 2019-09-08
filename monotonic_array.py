# 896. Monotonic Array

# An array is monotonic if it is either monotone increasing or decreasing.
#
# An array A is monotone increasing if:
#     for all i <= j, A[i] <= A[j]
# An array A is monotone decreasing if:
#     for all i <= j, A[i] >= A[j]
#
# Return true if and only if the given array A is monotonic.

# Examples:
# [1,2,2,3] => True
# [6,5,4,4] => True
# [1,3,2] => False
# [1,1,1] => True

# Analysis:
# N is len(A)
# Time: O(N)
# Space: O(1)


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_inc = is_dec = True

        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                is_inc = False
            if A[i-1] < A[i]:
                is_dec = False

        return is_inc or is_dec
