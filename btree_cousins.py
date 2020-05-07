"""
@lc id=993 lang=python3 tag=btree,binarytree

[993] Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Constraints:
    - The number of nodes in the tree will be between 2 and 100.
    - Each node has a unique integer value from 1 to 100.


Definition for a binary tree node:
    

Example 1:
  Input: x=4, y=3
      1
     / \
    2   3
   /
  4
  Output: false

Example 2:
  Input: x=4 y=5
       1
      / \
     2   3
      \   \
       4   5
  Output: true

Example 3:
  Input: x=2, y=3
      1
     / \
    2   3
     \ 
      4 
  Output: false

Complexity:
    Let: N = nodes in Binary tree, W = width of tree
    Time: O(N) -> BFS, worst case x and y are leaves
    Space: O(W) -> worst case O(N) for chubby tree
"""

from collections import deque


# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_cousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None or root.val == x or root.val == y:
            return False

        # BFS
        q, parents = deque([root]), []
        while q:
            n = len(q) 
            for _ in range(n): 
                curr = q.popleft()

                if curr.left is not None:
                    if curr.left.val == x or curr.left.val == y:
                        parents.append(curr)
                    else:
                        q.append(curr.left)

                if curr.right is not None:
                    if curr.right.val == x or curr.right.val == y:
                        parents.append(curr)
                    else:
                        q.append(curr.right)

            if len(parents) == 1: # different depths          
                return False
            elif len(parents) == 2: # same depths, check parents
                return parents[0] != parents[1]

        return False
