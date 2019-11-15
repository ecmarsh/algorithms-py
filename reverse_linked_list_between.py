"""
@=lc id=92 lang=python3 tag=linkedlist

[92] Reverse Linked List 2

Reverse a linked list from position m to n in one-pass.

Constraints:
   - `1 <= m <= n <= # nodes in list`


Example 1:
  Input: 1->2->3->4->5-None  m=2, n=4
Output: 1->4->3->2->5->None

Complexity:
  Time: O(n) one-pass, where n is nodes in list.
  Space: O(1) iterative one-pass only with pointers.
"""


class ListNode:
    """ Definition for singly-linked list """
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Edge cases requiring no traversal are
        # empty list, list with one node, or start == end.
        # Note length of one is handled by start == end.
        if not head or m == n:
            return head
        
        # Move the starting cursor to index m,
        # Keep prev as index before m to connect list after reversal.
        # Note prev must be set to None in case m is 1.
        cur, prev = head, None
        while m > 1: 
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        # Store the final connection nodes.
        connector, tail = prev, cur
        
        # Reverse the nodes to the end index, n.
        while n > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            n -= 1
        
        # Connect the list for beginning of reversal portion.
        if not connector:
            head = prev
        else:
            connector.next = prev
        
        # Connect the end of the reversal portion, breaking any cycles.
        tail.next = cur

        return head
