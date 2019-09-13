# 109. Convert Sorted List to Binary Search Tree
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.

# Example
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5],
# which represents the following height balanced BST:
#      0
#     / \
#   -3   9
#   /   /
# -10  5

# Analysis:
# N is size of list
# Time: O(N) (find size) + O(N) (construct tree) = O(2N) -> O(N)
# Space: O(log N) Stack space: Height balanced BST bound on log N

# Other solutions variants of:
# https://github.com/ecmarsh/algorithms/blob/master/exercises/sortedArrayToBST.js
# Find middle node each time and construct recursively:
#   O(N log N) time, O(log N space)
# Process elements to array and use same method as sortedArrToBST:
#   O(N) time and O(N) space for array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class TreeNode:
    " Def for binary tree node "
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getSize(self, head: ListNode) -> int:
        " Find length/size of linked list "
        if not head:
            return 0

        node, size = head, 0
        while (node):
            size += 1
            node = node.next

        return size

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.getSize(head)

        if size == 0:
            return None

        def constructBST(left: int, right: int) -> TreeNode:
            nonlocal head

            if left > right:
                return None

            # Not actually using middle node of list
            # Only using as indicators to signal termination
            mid = (left + right + 1) // 2

            # First step of simulated inorder traversal: form left half
            # Recursively form the left half
            left_node = constructBST(left, mid - 1)

            # Once left half is traversed, process current node as root
            root = TreeNode(head.val)
            root.left = left_node

            # Maintain invariance: after constructing left half,
            # head is either root or the middle (which becomes root)
            # so simply progress current value to next root
            head = head.next

            # Complete BST by recursively forming right-hand side
            root.right = constructBST(mid + 1, right)

            return root

        return constructBST(0, size - 1)
