# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def newTreeNode(start, end):
            slow = fast = start

            while True:
                if start == end:
                    return None
                if (fast and fast.next == end) or fast == end or (end and fast == end.next):
                    root = TreeNode(slow.val)
                    root.left = newTreeNode(start, slow)
                    root.right = newTreeNode(slow.next, end)

                    return root
                fast = fast.next.next
                slow = slow.next

        return newTreeNode(head, None)