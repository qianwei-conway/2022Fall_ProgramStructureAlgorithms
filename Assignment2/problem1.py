# 1. Symmetric Tree (https://leetcode.com/problems/symmetric-tree/)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode):

        p = q = root
        return self.check(root.left, root.right)

    def check(self, p, q):

        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val == q.val:
                return self.check(p.left, q.right) and self.check(p.right, q.left)
            else:
                return False