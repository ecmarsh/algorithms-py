"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA)
of two given nodes, p and q, in the BST.

According to the definition of LCA on Wikipedia:
  “The lowest common ancestor is defined between two nodes p and q
   as the lowest node in T that has both p and q as descendants
   (where we allow a node to be a descendant of itself).”

Constraints:
  - All of the node's values will be unique.
  - `p` and `q` are different and both values will exist in the BST.


Example:
Binary search tree: [6,2,8,0,4,7,9,null,null,3,5]
           6
         /   \
        2     8
       / \   / \
      0   4 7   9
         / \
        3   5

Input: p=2, q=8
Output: 6
Explanation: LCA of nodes 2 and 8 is 6

Input: p=4, q=2
Output: 2
Explanation: LCA is 2 since a node can be a descendant of itself.


Analysis:
Time: O(h) where h is height of tree.
      If we don't know height, use H->N relationship where N is nodes in tree:
        - Height balanced (chubby): log(N)
        - N-1 = N worst case if thin eg 5->4->3->2->1 given p = 1, q = 4
Space: O(1)
"""

# Definition for a binary tree node.
# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bst_lca(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        """
        If we consider the root, there are four possibilities:
            1. LCA is root if root is p or q
            2. LCA is root if p < root and q > root, (starts a branch).
            3. LCA is in left subtree if p and q both < root.
            4. LCA is in right subtree if p and q both > root.
        Note that this can only be done since keys are distinct.
            i.e:  p and q cannot hold equal keys.
        Otherwise, we must use same O(N) LCA find method of normal binary tree.
        """
        # Early return if option 1
        if root == p or root == q:
            return root

        # Ensure p is lower of two values for comparisons
        if p.val > q.val:
            p, q = q, p

        # Proceed with possibilities 3 or 4 until
        # root satisfies possibilities 1 or 2 --> LCA is root
        while root.val < p.val or root.val > q.val:
            # Although 3 and 4 specify both, we know p < q
            # so we only need to check p to go right, q to to left.
            # ie: if root less than p, then root is also less than q
            #     and if root is greater than q, its also greater than p.
            while root.val < p.val:
                root = root.right
            while root.val > q.val:
                root = root.left

        # 1, 2) p <= root <= q
        return root
