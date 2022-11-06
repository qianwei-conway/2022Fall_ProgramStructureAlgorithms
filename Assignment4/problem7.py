# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        if p.right:
            res = p.right
            while res.left:
                res = res.left
            return res

        res = None
        while root != p:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res
