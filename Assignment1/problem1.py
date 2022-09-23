# Definition for singly-linked list.
# 1. Rotate List (https://leetcode.com/problems/rotate-list/)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        cnt = 0
        while temp:
            cnt += 1;
            temp = temp.next;

        loc = k % cnt

        if loc == 0:
            return head
        else:
            slow = fast = head
            for i in range(loc):
                fast = fast.next
            while fast.next:
                slow, fast = slow.next, fast.next

            newHead = slow.next
            slow.next = None
            fast.next = head
            return newHead