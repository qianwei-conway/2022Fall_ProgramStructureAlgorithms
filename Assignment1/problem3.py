# Definition for singly-linked list.
# 3. Swapping Nodes in a Linked List(https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        fast = slow = head
        for _ in range(k - 1):
            fast = fast.next
        node1 = fast

        while fast.next:
            fast, slow = fast.next, slow.next
        node2 = slow

        temp = node2.val
        node2.val = node1.val
        node1.val = temp

        return head