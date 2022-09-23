# Definition for a Node.
# 5. Insert into a Sorted Circular Linked List(https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/)
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            head = ListNode(insertVal)
            head.next = head
            return head

        curr = head

        while curr.next != head:
            if curr.val <= curr.next.val:
                if insertVal >= curr.val and insertVal < curr.next.val:
                    newNode = ListNode(insertVal, curr.next)
                    curr.next = newNode
                    return head
                else:
                    curr = curr.next

            else:
                if insertVal >= curr.val or insertVal < curr.next.val:
                    newNode = ListNode(insertVal, curr.next)
                    curr.next = newNode
                    return head
                else:
                    curr = curr.next

        # If run to this line, it means all the nodes have the same value
        newNode = ListNode(insertVal, head)
        curr.next = newNode
        return head