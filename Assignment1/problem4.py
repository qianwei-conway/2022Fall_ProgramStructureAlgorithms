# Definition for singly-linked list.
# 4. Split Linked List in Parts (https://leetcode.com/problems/split-linked-list-in-parts/)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        cnt, temp = 0, head
        while temp:
            cnt += 1
            temp = temp.next

        res = []
        curr = head


        while cnt:
            subNum = (cnt + k - 1) // k
            res.append(curr)

            for _ in range(subNum - 1):
                curr = curr.next
            temp = curr.next
            curr.next = None
            curr = temp

            cnt -= subNum
            k -= 1
        while k:
            res.append(None)
            k -= 1

        return res