# 7. Lowest Common Ancestor of a Binary Tree (https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 1. Recursive Method
        #         if not root:
        #             return None
        #         if root == p or root == q:
        #             return root

        #         left = self.lowestCommonAncestor(root.left, p , q)
        #         right = self.lowestCommonAncestor(root.right, p, q)

        #         if not left and not right:
        #             return None
        #         if left and right:
        #             return root

        #         return left if left else right

        # 2. Iterative Method
        queue = [root]
        parent = {root: None}

        while p not in parent or q not in parent:

            node = queue.pop(0)

            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = []
        while p:
            ancestors.append(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q


