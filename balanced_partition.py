"""
@=lc id=1049 lang=python3 alias=balanced_partition tag=dp,knapsack,partition

[1049] Last Stone Weight II

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the
stones have weights x and y with x <= y.  The result of this smash is:
    - If x == y, both stones are totally destroyed;
    - If x != y, the stone of weight x is totally destroyed,
                 and the stone of weight y has new weight y-x.
                 
At the end, there is at most 1 stone left.
Return the smallest possible weight of this stone
(the weight is 0 if there are no stones left.)

Constraints:
    - `1 <= stones.length <= 30`
    - `1 <= stones[i] <= 100`


Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
    Combine 2 and 4 to get 2 -> [2,7,1,8,1]
    Combine 7 and 8 to get 1 -> [2,1,1,1]
    Combine 2 and 1 to get 1 -> [1,1,1]
    Combine 1 and 1 to get 0 -> [1]
    So the optimal value is 1


Complexity:
n is len(stones), s is sum of stones (capped at 3000 per constraints)
Time: O(n*s) DP calculation time for optimal partition.
Space: O(s/2) = O(s). Max will be 3000/2=1500
"""


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        Note what we are actually doing is partioning the array into
        2 subsets for minimal difference between the two.
        Then we cancel them out, the difference is the minimum value we can achieve.
        
        For the given example, [2,7,4,1,8,1], we could partition to:
        [1,1,2,7],sum=11 and [4,8], sum=12. We achieve same answer with diff (12-11)=1.
        
        For partioning explanation, see https://leetcode.com/problems/target-sum/
        
        We could also rephrase this as the 0/1 knapsack divide spoils.
        i.e. collecting some rocks, where the weights of the rocks is maximized
        and their total weight does not exceed half of the total weight of the rocks.
        """
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return max(stones)-min(stones)
        
        accSum = sum(stones)
        capacity = accSum >> 1
        weights = [0] * (capacity+1)
        
        # Maximize weights of rocks under capacity
        for stone in stones:
            for weight in range(capacity, -1, -1):
                if weight >= stone:
                    weights[weight] = max(stone+weights[weight-stone], weights[weight])
        
        # Return the difference between partitions
        totalWeightOfLesserPartition = 2 * weights[-1]
        return accSum - totalWeightOfLesserPartition

