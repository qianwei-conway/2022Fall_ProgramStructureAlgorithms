# Definition for singly-linked list.
# 2. Remove Linked List Elements (https://leetcode.com/problems/remove-linked-list-elements/)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # if the beginning is the given value, then...
        dummyHead = ListNode(0)
        dummyHead.next = head

        prev, curr = dummyHead, dummyHead.next

        while curr:
            if curr.val != val:
                prev, curr = prev.next, curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return dummyHead.next