# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # store the node before current node
        pred = None
        # store the two nodes need to be swapped
        node1 = node2 = None

        curr = root

        while curr:

            if not curr.left:
                if pred and pred.val > curr.val:
                    if not node1:
                        node1 = pred
                    node2 = curr
                pred = curr

                curr = curr.right

            else:
                predecessor = curr.left

                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = curr
                    curr = curr.left

                if predecessor.right == curr:
                    if pred and pred.val > curr.val:
                        if not node1:
                            node1 = pred
                        node2 = curr
                    pred = curr

                    predecessor.right = None
                    curr = curr.right

        node1.val, node2.val = node2.val, node1.val