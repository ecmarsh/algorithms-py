""" 703. Kth Largest Element In a Stream

Description:

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k
and an integer array nums, which contains initial elements from the stream.
For each call to the method KthLargest.add, return the element representing
the kth largest element in the stream.

You may assume that nums' length ≥ k-1 and k ≥ 1.

Your KthLargest object will be instantiated and called as such:
  obj = KthLargest(k, nums)
  param_1 = obj.add(val)


Example:
    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   # returns 4
    kthLargest.add(5);   # returns 5
    kthLargest.add(10);  # returns 5
    kthLargest.add(9);   # returns 8
    kthLargest.add(4);   # returns 8


Analysis (n is len(initial nums), k is k)
Init -> Time: nlargest=O(k + log(k) * (n - k)) to build heap || Space:O(k)
Add -> Time: Worst case log(k) if item is larger than current kthLargest.

"""

import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = heapq.nlargest(k, nums + [float('-inf')]*(k-len(nums)))
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        if val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
