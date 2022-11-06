# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 1. recursive
        def helper(root):
            nonlocal res
            if not root:
                return

            if low <= root.val <= high:
                res += root.val
            if low <= root.val:
                helper(root.left)
            if root.val <= high:
                helper(root.right)

        res = 0
        helper(root)
        return res

        ''' 2. Morris
        def _inorder(curr, res):
            # nonlocal res
            while curr:
                if not curr.left:
                    if curr.val >= low and curr.val <= high:
                        res += curr.val
                    curr = curr.right

                else:
                    predecessor = curr.left

                    while predecessor.right and predecessor.right != curr:
                        predecessor = predecessor.right

                    if not predecessor.right:
                        predecessor.right = curr
                        curr = curr.left

                    if predecessor.right == curr:
                        if curr.val >= low and curr.val <= high:
                            res += curr.val
                        predecessor.right = None
                        curr = curr.right

            return res

        return _inorder(root, 0)
        '''

